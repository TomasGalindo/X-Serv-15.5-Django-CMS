from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from cms.models import Pages


def pagina(request, identificador):
    if request.method == "GET":
        try:
            pagina = Pages.objects.get(id=identificador)
            respuesta = pagina.page
        except Page.DoesNotExist:
            respuesta = "No existe la pagina " + str(identificador)

    else:
        respuesta = "No puedes utilizar ese metodo. Puedes utilizar GET"

    return HttpResponse(respuesta)
