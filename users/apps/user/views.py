from django.shortcuts import render, redirect
from datetime import datetime
from .models import User
# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'user/users.html', context)

def createuser(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/')
    else:
        return redirect('/')
def create(request):
    return render(request,'user/usercreate.html')

def user(request, number):
    context = {
        'user': User.objects.get(id=number)
    }
    return render(request,'user/user.html', context)

def edit(request, number):
    context = {
        'user': User.objects.get(id=number)
    }
    return render(request,'user/useredit.html', context)

def update(request, number):
    if request.method == "POST":
        b = User.objects.get(id=number)
        b.first_name=request.POST['first_name']
        b.last_name=request.POST['last_name']
        b.email=request.POST['email']
        b.updated_at = datetime.now()
        b.save()
        return redirect('/users/'+number)
    else:
        return redirect('/')

def delete(request, number):
    b = User.objects.get(id=number)
    b.delete()
    return redirect('/')