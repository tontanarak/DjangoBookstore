from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from django.db.models import Sum
from django.contrib.auth.models import User,auth
from random import randint

# Create your views here.
message = ''

def index(request):
    data = Book.objects.all()     
    return render(request,'index.html',{'products':data})


def howtobuy(request):
    return render(request,'howtobuy.html')

def booklist(request):
   
    search = request.GET.get('search','')
    if search:
        data = Book.objects.filter(BookName__icontains=search)
    else:
        data = Book.objects.all()
    
    
    return render(request,'booklist.html',{'name':data})

def cart(request,userID):
    data = Payment.objects.filter(UserID=userID)
    cart = Cart.objects.filter(UserID=userID)
    book = Book.objects.all()
    total = str(Cart.objects.filter(UserID=userID).aggregate(Sum('CartPrice')))
    discont = 0.0
    if total[19:23] == "None": 
        total = 0
    elif cart.count()==0:
        total=0
    else : 
        total = float(total[19:].split('}')[0])
    Total = (total-discont)+60
    return render(request,'cart.html',{
        'Total':Total,
        'total':total,
        'discont':discont,
        'book':book,
        'cart':cart,
        'book':book,
        
        })

def addtocart(request,bookID,userID):
    qty = request.POST['qty']
    book = Book.objects.get(id=bookID)
    user = User.objects.get(id=userID)
    price = float(qty)*float(book.BookPrice)
    price = float(price)
    cart = Cart.objects.create(
        BookID=book,
        UserID=user,
        CartQty=qty,
        CartPrice=price,
    )
    cart.save()

    return redirect("/Cart/"+str(userID))

def deletecart(request,id,userID):
    deletecart = Cart.objects.filter(id=id).delete()
    return redirect("/Cart/"+str(userID))
    
def pay(request,ID):
    pay = Payment.objects.filter(UserID=ID)
    user = User.objects.filter(id=ID)
    
    return render(request,'payment.html',{'payment':pay,'xuser':user})

def confirmpayment(request):
    
    return render(request,'confirmpayment.html')
def payment(request):
    cfid = request.POST['cfid']
    name = request.POST['name']
    phone = request.POST['phonenumber']
    date = request.POST['date']
    price = request.POST['price']
    note = request.POST['note']
    cf = confirm.objects.create(
        payID=cfid,
        Name=name,
        phoneNo=phone,
        date=date,
        price=price,
        note=note,
    )

    cf.save()

    return render(request,'complete.html')

def paydetials(request,ID):
    payment  = Payment.objects.filter(index=ID)
    total = str(Payment.objects.filter(index=ID).aggregate(Sum('Total')))
    if total[14:20] == "None": 
        total = 0
    elif payment.count()==0:
        total=0
    else : 
        total = float(total[14:].split('}')[0])
    Total = total+60
    return render(request,'paydetails.html',{'payment':payment,'Total':Total,'paym':payment[0]})

def addpayment(request,userID):
    address = request.POST['address']
    cart = Cart.objects.filter(UserID=userID)
    total = str(Cart.objects.filter(UserID=userID).aggregate(Sum('CartPrice')))
    s = cart
    gen_id = randint(0,9999)
    if total[19:23] == "None": 
        total = 0
    elif cart.count()==0:
        total=0
    else : 
        total = float(total[19:].split('}')[0])
    Total = total+60
    for i in range(len(s)):
        
        pay = Payment.objects.create(
        index = gen_id,
        UserID=cart[0].UserID,
        Total =(s[i].BookID.BookPrice)*s[i].CartQty,
        Address = address,
        BookID=s[i].BookID,
        qty = s[i].CartQty
        
    )
    pay.save()
    total = 0
    delete = Cart.objects.filter(UserID=userID).delete()
    return redirect('/Payment/'+str(userID))

def book(request,bookID):
    
    data = Book.objects.get(id=bookID)
    if data.BookQty < 1 : 
        status = False
    else:
        status = True
    return render(request,'book.html',{'id':bookID,'products':data,'status':status})

def signup(request):
    return render(request,'signup.html')

def signin(request):
   
    return render(request,'signin.html')

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    password = request.POST['password']

    user = User.objects.create_user(
        username = username,
        password = password,
        first_name = firstname,
        last_name = lastname
    )

    user.save()


    return redirect('/')


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    
    user = auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return redirect('/')
    else :
        message = True
        return render(request,'signin.html',{'message': message})

def logout(request):
    auth.logout(request)
    return redirect('/')


