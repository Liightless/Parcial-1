from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido a la página de inicio</h1>")
