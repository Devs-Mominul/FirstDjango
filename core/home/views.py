from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"services.html")
def blog(request):
    return render(request,"blog.html")
def formGets(request):
    n3=0
    try:
        # n1=request.Get['num1']
        # n2=request.Get['num2']
        n1=int(request.Get.get('n1'))
        n2=int(request.Get.get('n2'))
        n3=n1+n2
     
    except:
        pass
    return render(request,"form.html",{"output":n3})
def postsubmit(request):
    return HttpResponse(request)
