from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect
#db name
from .models import place
from.models import people 



def demo(request):
    return render(request,"index.html")

#login.html
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")

#registration.html
def reg(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        #password verification
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('reg')
              
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('reg')
              
            else:
                myuser=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                myuser.save()  
                return redirect('login')
                print("user created")
         
        else:
            messages.info(request,"password not match")
            return redirect("reg")
        return redirect('/')
    return render(request,'register.html')

#logout code:
def logout(request):
    auth.logout(request)
    return redirect('/')






# Create your views here.
