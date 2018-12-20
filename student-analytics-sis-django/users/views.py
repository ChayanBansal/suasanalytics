from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request,username=username,password=pwd)
        #cursor.execute("SELECT COUNT(*) FROM Users WHERE username='"+username+"' AND password='"+hashlib.sha512(pwd.encode('UTF-8')).hexdigest()+"'")    
        if user:
            login(request,user)
            request.session['username']=username
            return render(request,'users/login.html',{"error":"Successufully logged in"})
        else:
            context={
                "error":"Please make sure your username and password is correct!"
            }
            return render(request,'users/login.html',context)
       
    else:
        return render(request,'users/login.html',{})

