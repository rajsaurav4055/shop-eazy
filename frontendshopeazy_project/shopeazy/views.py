from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.shortcuts import get_object_or_404
from django.contrib import messages
from shopeazy.models import User, Product, CartOrder, Cart, CartOrderItems
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.conf import settings


# Create your views here.
discounted_Price=None

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
        print(userid)
        messages.success(request, "You are successfully registered! Thank You.")
        return redirect('signin')
        

    return render(request, "shopeazy/signup.html")

def signin(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        # user = User.get_object_or_404(userid = userid)
        # user = User.objects.get(userid = userid)
        try:
            user = User.objects.get(userid = userid)
        except User.DoesNotExist:
            data ={}
            message= 'Invalid Credentials!'
            data['message'] = message
            return render(request, "shopeazy/signin.html", data)
        if user.userid == userid and user.password == password:
            context ={}
            context['user'] = user
            #adding the current user to the current session
            request.session['user'] = user.userid
            return redirect("homepage")
        # else:
        #     messages.error(request, "Wrong Credentials. Please try again!")
        #     return redirect('homepage',data)
        
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

def orderitems(request,id):
    order = CartOrder.objects.get(pk=id)
    user = User.objects.get(userid=request.session['user'])
    orderitems = CartOrderItems.objects.filter(order=order)
    return render(request, "shopeazy/orderitems.html",{'orderitems':orderitems, 'user': user,'order':order})

def orderlist(request):
    user = User.objects.get(userid=request.session['user'])
    orders=CartOrder.objects.filter(user=user)
    return render(request, "shopeazy/orderlist.html",{'orders':orders, 'user': user})

def add_to_cart(request):
    # del request.session['cartdata']
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
            print(item)
            total_amt+=int(item['qty'])*int(item['price'])
        return render(request, "shopeazy/cart.html",{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
    else:
        return render(request, "shopeazy/cart.html",{'cart_data':'','totalitems':0,'total_amt':total_amt})

def product(request, id):
    product = Product.objects.get(productid = id)
    relatedProducts = Product.objects.filter(category = product.category)
    return render(request, "shopeazy/product.html", {'relatedProducts':relatedProducts, 'product':product})


def delete_cart_item(request):
    p_id=str(request.GET['id'])
    if 'cartdata' in request.session:
        if p_id in request.session['cartdata']:
            cart_data = request.session['cartdata']
            del request.session['cartdata'][p_id]
            request.session['cartdata']=cart_data
    total_amt=0
    for p_id,item in request.session['cartdata'].items():
            print(item)
            total_amt+=int(item['qty'])*int(item['price'])
    t=render_to_string('shopeazy/ajax/cart-list.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
    return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})



def get_discounted_price(request):
    global discounted_Price 
    discounted_Price = request.GET['price_after_discount']
    print("Inside getDiscountPrice function "+ discounted_Price)
    return JsonResponse({'data':discounted_Price})

#checkout page
def checkout(request):
    
    if ('user' in request.session):
        print("logged in")
        
        # address=UserAddressBook.objects.filter(user=request.user,status=True).first()
        # return render(request, 'checkout.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'form':form,'address':address})
        total_amt=0
        print("entered checkout page")
        print(discounted_Price)
        # final_price= get_discounted_price(request)
        # print(final_price)
        if 'cartdata' in request.session:
            print("after cart")
            #Order
            user = User.objects.get(userid=request.session['user'])
            order = CartOrder.objects.create(user=user,finalprice=discounted_Price)
            for productid,item in request.session['cartdata'].items():
                print(item)
                total_amt+=int(item['qty'])*int(item['price'])
                #OrderItems
                items = CartOrderItems.objects.create(
                    order=order,
                    invoice_number='INV-'+str(order.id),
                    item=item['pname'],
                    image=item['image'],
                    qty=item['qty'],
                    price=item['price'],
                    total=int(item['qty'])*int(item['price'])
                )

            #process payment
            host = request.get_host()
            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount': discounted_Price,
                'item_name': 'OrderNo-'+str(order.id),
                'invoice': 'INV-'+str(order.id),
                'currency_code': 'CAD',
                'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
                'return_url': 'http://{}{}'.format(host,reverse('payment_done')),
                'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
            return render(request, "shopeazy/checkout.html",{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':discounted_Price,'form':form})
    else:
        return render(request,"shopeazy/signin.html" )

def search(request):
    query=request.GET['query']
    data = Product.objects.filter(pname__icontains=query)
    return render(request, "shopeazy/search.html",{'data':data})

@csrf_exempt
def payment_done(request):
    returnData=request.POST
    del request.session['cartdata']
    return render(request, 'shopeazy/paymentsuccess.html',{'data':returnData})


@csrf_exempt
def payment_cancelled(request):
	return render(request, 'shopeazy/paymentfailed.html')


