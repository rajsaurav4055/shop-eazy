from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "shopeazy/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST.get('firstname',False)
        lastname = request.POST.get('lastname', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        confirmpassword = request.POST.get('confirmpassword',False)

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request, "You are successfully registered! Thank You.")

        return redirect('signin')

    return render(request, "shopeazy/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username',False)
        password = request.POST.get('password', False)

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "shopeazy/index.html", {'firstname' : firstname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request, "shopeazy/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')            