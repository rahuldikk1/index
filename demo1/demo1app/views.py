from django.shortcuts import render

from .models import place


def demo(request):
     obj=place.objects.all()
     return render(request,"index.html",{'result':obj})
# def operation(request):
#      a=int(request.GET['num1'])
#      b=int(request.GET['num2'])
#      res=(a+b)
#      a = int(request.GET['num1'])
#      b = int(request.GET['num2'])
#      res1 = (a*b)
#      a = int(request.GET['num1'])
#      b = int(request.GET['num2'])
#      res2 = (a/b)
#      a = int(request.GET['num1'])
#      b = int(request.GET['num2'])
#      res3 = (a-b)
#      return render(request, "result.html", {'result': res,'result1':res1,'result2':res2,'result3':res3})
