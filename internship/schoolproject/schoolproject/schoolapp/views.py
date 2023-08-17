from django.http import HttpResponse
from django.shortcuts import render
from . models import destination
from . models import team

# Create your views here.
def demo(request):
    obj=destination.objects .all()
    obj1 = team.objects.all()
    # name="india"
    return render(request,"index.html",{'result':obj ,'res':obj1})

    # name="india
# def about (request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("am contact")