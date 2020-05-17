from django.shortcuts import render,redirect
from .models import project, Message

def home(request):
    job = project.objects
    if request.method == 'POST':
        if request.POST['name'] and request.POST['email'] and request.POST['subject'] and request.POST['memo']:
            cont= Message()
            cont.name = request.POST['name']
            cont.email = request.POST['email']
            cont.subject = request.POST['subject']
            cont.memo = request.POST['memo']
            cont.save()
            return redirect('home')
        else:
            return render(request, 'main/home.html',{'error':"All fields Manditory"})
    else:
            return render(request, 'main/home.html',{'job':job})