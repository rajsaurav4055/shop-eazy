from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
from shopeazy.models import User, Product, Order, Cart


# Create your views here.
'''def home(request):
    return render(request, "shopeazy/homepage.html")'''

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
            return redirect('homepage')
        if User.objects.filter(email = email):
            messages.error(request, "Email already registered!")
            return redirect('homepage')
        if password != confirmpassword:
           messages.error(request, "Password doesn't match!")
           return redirect('homepage')
        if len(phoneno)!= 10:
            messages.error(request, "Enter correct 10 digit phone number")
            return redirect('homepage')
        
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
            context ={}
            context['user'] = user
            #adding the current user to the current session
            request.session['user'] = user.userid
            return redirect("homepage")
        else:
            messages.error(request, "Wrong Credentials. Please try again!")
            return redirect('homepage')
        
    return render(request, "shopeazy/signin.html")

def signout(request):
    #clearing the current session
    request.session.clear()
    messages.success(request, "Logged Out Successfully!")
    return redirect('homepage')    

def category_homepage(request, category):
    context={}
    products = Product.objects.filter(category = category)
    context['products'] = products
    return render(request, "shopeazy/homepage.html",context)

def homepage(request):
    context={}
    products = Product.objects.all()
    context['products'] = products
    return render(request, "shopeazy/homepage.html",context)

def order(request):
    pass

def add_to_cart(request):
    cart_p={}
    cart_p[str(request.GET['productid'])]={
		'image':request.GET['image'],
		'pname':request.GET['pname'],
		'qty':request.GET['qty'],
		'price':request.GET['price'],
	}
    print("inside add to cart")
    if 'cartdata' in request.session:
        if str(request.GET['productid']) in request.session['cartdata']:
            cart_data=request.session['cartdata']
            cart_data[str(request.GET['productid'])]['qty']=int(cart_p[str(request.GET['productid'])]['qty'])
            cart_data.update(cart_data)
            request.session['cartdata']=cart_data
        else:
            cart_data=request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata']=cart_data
    else:
        request.session['cartdata']=cart_p
    return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})

def cart(request):
    total_amt=0
    print("before cart")
    if 'cartdata' in request.session:
        print("after cart")
        for productid,item in request.session['cartdata'].items():
            total_amt+=int(item['qty'])*float(item['price'])
        return render(request, "shopeazy/cart.html",{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
    else:
        return render(request, "shopeazy/cart.html",{'cart_data':'','totalitems':0,'total_amt':total_amt})

def product(request):
    pass