from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html',{'bands':bands})

def about(request):
    return HttpResponse('<h1>A propos!</h1><p>Nous adorons merch!!</p>')

def list(request):
    return HttpResponse('<h1>La liste des produits</h1>')

def contact(request):
    return HttpResponse('<h1>Contactez nous!</h1>\
                        <label>Votre message: </label><input type="textarea" placeholder="réagissez"/>')
