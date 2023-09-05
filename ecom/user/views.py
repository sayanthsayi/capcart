from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django . contrib.auth import login,logout,authenticate
from django . contrib. auth .models import User
from django. contrib.auth.decorators import login_required
# Create your views here.


def UserSignup(request):
    form = UserCreationForm()
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.capitalize()
            user.save()
            login(request,user)
            messages.success(request,'Signup Successfully')
            return redirect("home")
    context = {'form':form}
    return render(request,'usersignup.html',context)


def UserLogin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Login successfully')
            return redirect('home')
        else:
            messages.error(request,'something went wrong')
    return render(request,'login.html')

@login_required(login_url='signup')
def ConfirmLogout(request):
    return render(request,"logoutconfirm.html")

@login_required(login_url='signup')
def UserLogout(request):
    logout(request)
    return redirect('login')