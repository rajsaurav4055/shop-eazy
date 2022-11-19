from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
from shopeazy.models import User


# Create your views here.
def home(request):
    return render(request, "shopeazy/index.html")

def signup(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        if User.objects.filter(userid = userid):
            messages.error(request, "User ID already exists!")
            return redirect('home')
        if User.objects.filter(email = email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        if password != confirmpassword:
           messages.error(request, "Password doesn't match!")
           return redirect('home')
        if len(phoneno)!= 10:
            messages.error(request, "Enter correct 10 digit phone number")
            return redirect('home')
        
        user = User.objects.create(userid = userid,fname = fname,lname = lname,email = email,address = address,phoneno = phoneno,password = password)
        user.save()
        messages.success(request, "You are successfully registered! Thank You.")
        return redirect('signin')
        

    return render(request, "shopeazy/signup.html")

def signin(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        
        user = User.objects.get(userid = userid)
        
        if user.userid == userid and user.password == password:
            firstname = user.fname
            return render(request, "shopeazy/index.html", {'firstname': firstname})
        else:
            messages.error(request, "Wrong Credentials. Please try again!")
            return redirect('home')
        
    return render(request, "shopeazy/signin.html")

def signout(request):
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')    

def homepage(request):
    pass

def order(request):
    pass

def cart(request):
    pass

def product(request):
    return render(request, "shopeazy/product.html")