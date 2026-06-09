import json
from django.http import JsonResponse
from django.shortcuts import render

def home_view(request):
    return render(request, "index.html")


def validar(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data.get("username", "")
        password = data.get("password", "")

        if username == "admin" and password == "1234":
            return JsonResponse({
                "success": True,
                "message": "Login correcto: bienvenido admin.",
                "role": "admin"
            })
        elif username == "usuario" and password == "1234":
            return JsonResponse({
                "success": True,
                "message": "Login correcto: bienvenido usuario.",
                "role": "user"
            })
        else:
            return JsonResponse({
                "success": False,
                "message": "Credenciales inválidas."
            })

    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")
