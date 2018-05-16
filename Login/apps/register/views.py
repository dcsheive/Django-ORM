from django.shortcuts import render, redirect
from .models import User
import bcrypt
import re

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
    err = False
    email = request.POST['email']
    first = request.POST['first_name']
    last = request.POST['last_name']
    passw = request.POST['password']
    passc = request.POST['passcom']
    if email or first or last:
        request.session['email'] = email
        request.session['first_name'] = first
        request.session['last_name'] = last
    if len(email) < 1 or len(first) < 1 or len(last) <1 or len(passw)<1 or len(passc)<1:
        err = True
    if not EMAIL_REGEX.match(email):
        request.session['email'] = ''
        err = True
    if User.objects.filter(email__contains=email):
        err = True
    if passw != passc:
        err = True
    if len(passw) < 8 and passc and passw:
        err = True
    if not first.isalpha() and first: 
        request.session['first_name'] = ''
        err = True
    if not last.isalpha() and last:
        request.session['last_name'] = ''
        err = True
    if err==True:
        return redirect('/')
    pw_hash = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())  
    a = User(first_name=first, last_name = last, email = email, password = pw_hash)
    a.save()
    request.session.clear()
    request.session['id'] = User.objects.get(email=email).id
    return redirect('/success')

def login(request):
    email = request.POST['email']
    passw = request.POST['password']
    if len(passw) < 1 or len(email) < 1:
        return redirect('/')
    result = User.objects.get(email=email)
    if result.password:
        if bcrypt.checkpw(passw.encode(), result.password.encode()):
            request.session['id'] = result.id
            return redirect('/success')
    return redirect('/')


def home(request):
    if 'id' not in request.session:
        return redirect('/')
    request.session['fname'] = User.objects.get(id=request.session['id']).first_name
    return render(request, "register/home.html")

def logout(request):
    request.session.clear()
    return redirect('/')
