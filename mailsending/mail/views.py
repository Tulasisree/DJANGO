from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from mailsending import settings
from .forms import UserRegistrationForm

# Create your views here.

def home(request):
    return render(request,'mail/home.html')

def register(request):
    if request.method == 'POST':
        fname=request.POST['f_name']
        lname=  request.POST['l_name']
        uname=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']
        user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pwd)
        
        sub = 'UserAccount'
        body = 'Welcome to my Project \n This is your username:-'+uname+"\n Your Password is :-"+pwd
        receiver = email
        sender = settings.EMAIL_HOST_USER
        send_mail(sub,body,sender,[receiver])
        return redirect('/')

    return render(request,'mail/register.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form['username'].value()
            password = form['password1'].value()
            email = form['email'].value()
            sub = 'UserAccount'
            body = 'Welcome to my ModelForms \n This is your username:-'+username+"\n Your Password is :-"+password+'\nurl link : http://127.0.0.1:8000/'
            receiver = email
            sender = settings.EMAIL_HOST_USER
            send_mail(sub,body,sender,[receiver])
            return redirect('/')
    form = UserRegistrationForm
    return render(request,'mail/signup.html',{'form':form})