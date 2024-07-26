from django.shortcuts import render

def inicio(resquest):
    return render(resquest, "inicio.html", {})

def compra(resquest):
    return render(resquest, "compra.html", {})

def pago(resquest):
    return render(resquest, "pago.html", {})