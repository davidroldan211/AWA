from django.shortcuts import render
from sistema_awa.models import awa
from django.http import HttpResponse
# Create your views here.
def mostrarvariables(request):
     obj= awa.objects.last()
     return HttpResponse(obj)
     
     #render(request,'ver.html',{"obj":obj})

def sistema(request):
     obj=awa.objects.last()
     return render(request,"html/mi_sistema.html", {"obj":obj})