from django.http import HttpResponse


def index(request):
    return HttpResponse('Backed app is working.')
