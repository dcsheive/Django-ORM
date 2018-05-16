from django.shortcuts import render, redirect
from datetime import datetime
from .models import Course
# Create your views here.
def index(request):
    context = {
        'course': Course.objects.all() ,
    }
    return render(request,'courses/index.html', context)

def create(request):
    if request.method == "POST":
        a = Course(name=request.POST['name'], text=request.POST['text'])
        a.save()  
        return redirect('/courses')
    else:
        return redirect('/courses')

def delete(request,number):
    context = {
        'course': Course.objects.get(id=number)
    }
    return render(request,'courses/course.html', context)

def deletecourse(request, number):
    b = Course.objects.get(id=number)
    b.delete()
    return redirect('/courses')