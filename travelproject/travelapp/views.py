from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def travel(request):
    obj=Place.objects.all()
    teamobj=Team.objects.all()
    return render(request,"index.html",{'result':obj,'teamres':teamobj})


#def about(request):
#    return render(request,"about.html")

#def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    return render(request,"about.html",{'result':res})