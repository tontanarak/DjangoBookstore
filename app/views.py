from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from django.contrib.auth.models import User,auth
# Create your views here.
message = ''

def index(request):
    data = Book.objects.all()     
    return render(request,'index.html',{'products':data})

def Payment(request):
    return render(request,'Payment.html')

def Delivery(request):
    return render(request,'Delivery.html')

def booklist(request):
    data = Book.objects.all()
    return render(request,'booklist.html',{'name':data})

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

def AddUser(request):
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


