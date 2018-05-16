from django.shortcuts import render, redirect
from .models import User
import bcrypt
import re
from django.contrib import messages
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    if 'first_name' not in request.session:
        request.session['first_name'] = ""
    if 'last_name' not in request.session:
        request.session['last_name'] = ""
    if 'email' not in request.session:
        request.session['email'] = ""
    return render(request, "register/index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.reg(request.POST)
        email = request.POST['email']
        first = request.POST['first_name']
        last = request.POST['last_name']
        passw= request.POST['password']
        if email or first or last:
            request.session['email'] = email
            request.session['first_name'] = first
            request.session['last_name'] = last
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())  
            a = User(first_name=first, last_name = last, email = email, password = pw_hash)
            a.save()
            request.session.clear()
            request.session['id'] = User.objects.get(email=email).id
            return redirect('/success')
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.log(request.POST)
        email = request.POST['email']
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            request.session['id'] = User.objects.get(email=email).id
            return redirect('/success')
    else:
        return redirect('/')
    



def home(request):
    if 'id' not in request.session:
        return redirect('/')
    request.session['fname'] = User.objects.get(id=request.session['id']).first_name
    return render(request, "register/home.html")

def logout(request):
    request.session.clear()
    return redirect('/')
