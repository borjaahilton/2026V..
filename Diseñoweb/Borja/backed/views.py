from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('Backed app is working.')


def ejemplo_api(request):
    data = {
        "status": "success",
        "message": "Esta es una nueva URL en el backend de Django",
        "data": {
            "key": "value"
        }
    }
    return JsonResponse(data)


def login(request):
    return JsonResponse({"message": "Login endpoint"})


def register(request):
    return JsonResponse({"message": "Register endpoint"})


def logout(request):
    return JsonResponse({"message": "Logout endpoint"})


def reset_password(request):
    return JsonResponse({"message": "Reset password endpoint"})


def change_password(request):
    return JsonResponse({"message": "Change password endpoint"})


def forgot_password(request):
    return JsonResponse({"message": "Forgot password endpoint"})


def reset_password_confirm(request):
    return JsonResponse({"message": "Reset password confirm endpoint"})

