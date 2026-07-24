from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

