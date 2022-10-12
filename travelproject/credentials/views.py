from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login.html')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST["firstname"]
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                print("username already taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                print("email alrerady taken")
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,email=email,password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            print("password not matching")
            return redirect('registration')
        return redirect('/')
    return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')