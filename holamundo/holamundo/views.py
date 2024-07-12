from django.http import HttpResponse

def Saludo(request):
    return HttpResponse("Hola mundo")
     
def despedida(request):
    return HttpResponse("Adios carnal no estas haciendo super bien")


def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("eres mayor de edad")
    else:
        return HttpResponse("NO eres mayor de edad")