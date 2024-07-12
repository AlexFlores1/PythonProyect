from django.http import HttpResponse

def Saludo(request):
    return HttpResponse("Hola mundo")
     
def despedida(request):
    return HttpResponse("Adios carnal no estas haciendo super bien")