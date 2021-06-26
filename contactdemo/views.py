from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import fromfordemo
from django.contrib import messages
# Create your views here.
def homepage(request):
    return render(request,template_name='webtemp/home.html')
def about(request):
    return render(request,template_name='webtemp/about.html')
def project(request):
    return render(request,template_name='webtemp/project.html')

def contactform(request):
    
    if request.method == 'POST':
        name= request.POST.get('name')
        email_id= request.POST.get('email_id')
        phoneno= request.POST.get('phoneno')
        content= request.POST.get('content')
        instance=fromfordemo(name=name, email_id=email_id, phoneno=phoneno, content=content)
        instance.save()
        messages.success(request, 'Your Information has been submitted successfully.Thank You!')
        
        return redirect(request.path)
    else:
        return render(request, template_name='webtemp/contact.html')
    
