from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={ #dictonary
        "variable1":"this is sent",
        "variable2":"this is recieved"
    }
    
    return render(request, 'index.html',context)
    
def about(request):
    #return HttpResponse("this is about page")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("this is services page")
    return render(request, 'services.html')

def contact(request):
    #writing logic of adding contact in database
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')#POST is a dictionary
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.') #this is for confirming submission
    return render(request, 'contact.html')
    