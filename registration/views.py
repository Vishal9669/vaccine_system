from datetime import date, timedelta
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import registrat , child
from django.contrib import auth

# Create your views here.
def register(request):
    return render(request, 'register.html')

def registration(request):
    if request.method=="POST":
        email=request.POST['email']
        unm=request.POST['username']
        pwd=request.POST['password']
        try:
            user=User.Objects.get(username=unm)
            return render(request,'register.html',{'error':"username already exist...!!!"})
        except:
           user=User.objects.create_user(email=email,username=unm,password=pwd,)
           user.save()
           return render(request,'login.html',{'msg':"registered sucessfully"})
    else:
        return render(request,'register.html',{'error':"invaild user request"})

def login(request):
    return render(request, 'login.html')

def welcome(request):
    return render(request, 'welcome.html')

def loginpage(request):
    if request.method=="POST":
        unm=request.POST['Username']
        pwd=request.POST['password']
        user=auth.authenticate(username=unm,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'welcome.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def addnewchild(request):
    return render(request, 'addnewchild.html')

def logout(request):
    return render(request, 'logout.html')

def viewchild(request):
    return render(request, 'viewchild.html')
def addchild(request):
    if request.method=='POST':
        parent_name=request.POST['parent']
        name=request.POST['name']
        weight=request.POST['weight']
        bg=request.POST['blood_group']
        email=request.POST['email']
        dob=request.POST['dob']
        obj= child(parent=parent_name,name=name,weight=weight,blood_group=bg,email=email,dob=dob)
        obj.save()
        return render(request, 'viewchild.html')
def showdetails(request):
    details = child.objects.all()
    return render(request, 'showdetails.html',{'child':details})

def edit(request,id):
    details = child.objects.get(id=id)
    return render(request, 'edit.html',{'details':details})

def update(request,id):
    obj1 = child.objects.get(id=id)
    obj1.parent = request.POST['parent']
    obj1.name = request.POST['name']
    obj1.email = request.POST['email']
    obj1.weight = request.POST['weight']
    obj1.blood_group = request.POST['blood_group']
    obj1.dob = request.POST['dob']
    obj1.save()
    return redirect('/showdetails')

def delete(request,id):
    object= child.objects.get(id=id)
    object.delete()
    return redirect('/showdetails')

def vaccine(request, id):
    now = date.today()

    childData = child.objects.get(id=id)
    a = childData.dob

    v1 = a + timedelta(days=42)
    d1 = now - v1
    d1 = int(d1.days)

    v2 = a + timedelta(days=70)
    d2 = now - v2
    d2 = int(d2.days)

    v3 = a + timedelta(days=98)
    d3 = now - v3
    d3 = int(d3.days)

    v4 = a + timedelta(days=180)
    d4 = now - v4
    d4 = int(d4.days)

    v5 = a + timedelta(days=274)
    d5 = now - v5
    d5 = int(d5.days)

    v6 = a + timedelta(days=360)
    d6 = now - v6
    d6 = int(d6.days)

    v7 = a + timedelta(days=457)
    d7 = now - v7
    d7 = int(d7.days)

    v8 = a + timedelta(days=480)
    d8 = now - v8
    d8 = int(d8.days)

    v9 = a + timedelta(days=540)
    d9 = now - v9
    d9 = int(d9.days)

    v10 = a + timedelta(days=730)
    d10 = now - v10
    d10 = int(d10.days)

    v11 = a + timedelta(days=1620)
    d11 = now - v11
    d11 = int(d11.days)

    v12 = a + timedelta(days=3652)
    d12 = now - v12
    d12 = int(d12.days)
    return render(request, 'vaccine.html', {'v1': v1, 'v2': v2, 'v3': v3, 'v4': v4, 'v5': v5, 'v6': v6, 'v7': v7, 'v8': v8,
                   'v9': v9, 'v10': v10, 'v11': v11, 'v12': v12, 'details': childData,
                   'd1': d1, 'd2': d2, 'd3': d3, 'd4': d4, 'd5': d5, 'd6': d6,
                   'd7': d7, 'd8': d8, 'd9': d9, 'd10': d10, 'd11': d11,
                   'd12': d12})

def passwordform(request):
    return render(request, 'passwordform.html')

def passwordchange(request,id):
    user =User.objects.get(id=id)
    old_pwd= request.POST['old_password']
    pwd = request.POST['password']
    user.save()
    return render(request, 'pwdchanged.html')

