from django.http import HttpResponse, HttpResponseNotAllowed, QueryDict, JsonResponse
from django.shortcuts import render


from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
import json

from frejolito.models import Persona
from panel.models import Rol, Permiso, DetalleRol, DetallePermiso
from backed.models import Categoria, Marca, Proveedor, Descuento, Producto, Carrito, DetalleCarrito, Pedido, DetallePedido, Pago

def dashboard(request):
    context = {
        'per': Persona.objects.all(),
        'rol': Rol.objects.all(),
        'permiso': Permiso.objects.all(),
        'perfiles': DetalleRol.objects.all(),
        'detallepermiso': DetallePermiso.objects.all(),
        'categorias': Categoria.objects.all(),
        'marcas': Marca.objects.all(),
        'proveedores': Proveedor.objects.all(),
        'descuentos': Descuento.objects.all(),
        'productos': Producto.objects.all(),
        'carritos': Carrito.objects.all(),
        'detallecarritos': DetalleCarrito.objects.all(),
        'pedidos': Pedido.objects.all(),
        'detallepedidos': DetallePedido.objects.all(),
        'pagos': Pago.objects.all(),
    }
    return render(request, 'dashboard.html', context)


@csrf_exempt
def api_crud(request, model_name):
    # Mapeo de nombres sencillos a sus respectivos modelos y apps
    model_mapping = {
        'persona': ('frejolito', 'Persona'),
        'rol': ('panel', 'Rol'),
        'permiso': ('panel', 'Permiso'),
        'detallerol': ('panel', 'DetalleRol'),
        'detallepermiso': ('panel', 'DetallePermiso'),
        'categoria': ('backed', 'Categoria'),
        'marca': ('backed', 'Marca'),
        'proveedor': ('backed', 'Proveedor'),
        'descuento': ('backed', 'Descuento'),
        'producto': ('backed', 'Producto'),
        'carrito': ('backed', 'Carrito'),
        'detallecarrito': ('backed', 'DetalleCarrito'),
        'pedido': ('backed', 'Pedido'),
        'detallepedido': ('backed', 'DetallePedido'),
        'pago': ('backed', 'Pago'),
    }
    
    mapped = model_mapping.get(model_name.lower())
    if not mapped:
        return JsonResponse({'success': False, 'message': 'Modelo no encontrado.'}, status=404)
        
    app_label, model_class_name = mapped
    try:
        model_cls = apps.get_model(app_label, model_class_name)
    except LookupError:
        return JsonResponse({'success': False, 'message': 'Modelo no registrado.'}, status=404)
        
    if request.method == 'GET':
        obj_id = request.GET.get('id')
        if obj_id:
            try:
                obj = model_cls.objects.get(pk=obj_id)
                return JsonResponse({'success': True, 'data': serialize_model(obj)})
            except model_cls.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Objeto no encontrado.'}, status=404)
        
        # Listar todo
        objects = model_cls.objects.all()
        data_list = [serialize_model(obj) for obj in objects]
        return JsonResponse({'success': True, 'data': data_list})
        
    elif request.method == 'POST':
        try:
            body_data = json.loads(request.body)
        except json.JSONDecodeError:
            body_data = request.POST.dict()
            
        obj_id = body_data.get('id')
        
        try:
            # Caso especial para Persona que involucra User de Django
            if model_class_name == 'Persona':
                from django.contrib.auth.models import User
                username = body_data.get('username')
                email = body_data.get('email', '')
                first_name = body_data.get('first_name', '')
                last_name = body_data.get('last_name', '')
                password = body_data.get('password')
                
                if obj_id:
                    persona = model_cls.objects.get(pk=obj_id)
                    user = persona.usuario
                    user.username = username
                    user.email = email
                    user.first_name = first_name
                    user.last_name = last_name
                    if password:
                        user.set_password(password)
                    user.save()
                else:
                    if User.objects.filter(username=username).exists():
                        return JsonResponse({'success': False, 'message': 'El nombre de usuario ya existe.'}, status=400)
                    user = User.objects.create_user(username=username, password=password or '1234', email=email, first_name=first_name, last_name=last_name)
                    persona = model_cls(usuario=user)
                    
                persona.dni = body_data.get('dni')
                persona.telefono = body_data.get('telefono', '')
                persona.direccion = body_data.get('direccion', '')
                persona.es_activo = str(body_data.get('es_activo', 'true')).lower() in ['true', 'on', '1']
                persona.save()
                return JsonResponse({'success': True, 'data': serialize_model(persona)})
                
            # Resto de modelos
            if obj_id:
                obj = model_cls.objects.get(pk=obj_id)
            else:
                obj = model_cls()
                
            from django.db import models
            for field in model_cls._meta.fields:
                if not field.editable or field.primary_key:
                    continue
                name = field.name
                if name in body_data:
                    val = body_data[name]
                    if isinstance(field, models.ForeignKey):
                        if val:
                            related_model = field.remote_field.model
                            obj_ref = related_model.objects.get(pk=val)
                            setattr(obj, name, obj_ref)
                        else:
                            setattr(obj, name, None)
                    elif isinstance(field, models.BooleanField):
                        setattr(obj, name, str(val).lower() in ['true', 'on', '1'])
                    elif val == "" and field.null:
                        setattr(obj, name, None)
                    else:
                        setattr(obj, name, val)
            obj.save()
            return JsonResponse({'success': True, 'data': serialize_model(obj)})
            
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
            
    elif request.method == 'DELETE':
        obj_id = request.GET.get('id')
        if not obj_id:
            try:
                body_data = json.loads(request.body)
                obj_id = body_data.get('id')
            except:
                pass
        if not obj_id:
            return JsonResponse({'success': False, 'message': 'ID no provisto.'}, status=400)
            
        try:
            obj = model_cls.objects.get(pk=obj_id)
            if model_class_name == 'Persona' and obj.usuario:
                obj.usuario.delete()
            else:
                obj.delete()
            return JsonResponse({'success': True, 'message': 'Registro eliminado correctamente.'})
        except model_cls.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Registro no encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
            
    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)


def serialize_model(obj):
    from django.db import models
    data = {}
    for field in obj._meta.fields:
        val = getattr(obj, field.name)
        if val is None:
            data[field.name] = ""
        elif isinstance(field, (models.CharField, models.TextField, models.UUIDField)):
            data[field.name] = str(val)
        elif isinstance(field, (models.IntegerField, models.DecimalField, models.FloatField)):
            data[field.name] = float(val) if isinstance(field, models.DecimalField) else val
        elif isinstance(field, models.BooleanField):
            data[field.name] = val
        elif hasattr(val, 'isoformat'):
            data[field.name] = val.isoformat()
        elif isinstance(field, models.ForeignKey):
            data[field.name] = str(val.id) if hasattr(val, 'id') else (val.pk if val else "")
            data[f"{field.name}_str"] = str(val)
        else:
            data[field.name] = str(val)
            
    if obj.__class__.__name__ == 'Persona':
        data['username'] = obj.usuario.username
        data['email'] = obj.usuario.email
        data['first_name'] = obj.usuario.first_name
        data['last_name'] = obj.usuario.last_name
        
    return data

def user_dashboard(request):
    return render(request, 'user_dashboard.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == '1234':
            return JsonResponse({
                'success': True,
                'message': 'Login correcto: bienvenido admin.',
                'role': 'admin'
            })
        elif username == 'usuario' and password == '1234':
            return JsonResponse({
                'success': True,
                'message': 'Login correcto: bienvenido usuario.',
                'role': 'user'
            })
        return JsonResponse({
            'success': False,
            'message': 'Credenciales inválidas.'
        }, status=401)

    if request.method == 'PUT':
        data = QueryDict(request.body.decode('utf-8'))
        username = data.get('username', '')
        return HttpResponse(f'PUT recibido. Usuario enviado: {username}')

    if request.method == 'DELETE':
        return HttpResponse('DELETE recibido. Recurso eliminado (simulado).')

    return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])