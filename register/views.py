from django.shortcuts import render,redirect
from .forms  import *
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def main(request):
    return render(request,"register/main.html")
def courses(request):
    courses=Courses.objects.all()
    context={
        'courses':courses
    }
    return render(request,"register/courses.html",context)
def coursesSchedules(request):
    return render(request,"register/coursesSchedules.html")
def students(request):
    student=Students.objects.all()
    context={
        "student":student,
    }
    return render(request,"register/students.html",context)
def studentsReg(request):
    return render(request,"register/studentsReg.html")
def create(request):
    form=createNewUser()
    if request.method=='POST':
        form=createNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form':form
    }
    return render(request,'register/create.html',context)
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user=authenticate(request, username=username, password=password)
        if user is not None:
            print('saif')
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
    return render(request, 'register/login.html')
def createCourse(request):
    form=CourseForm()
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    context={
        'form':form
    }
    return render(request,'register/courseForm.html',context)
def deleteCourse(request,pk):
    course=Courses.objects.get(id=pk)
    if request.method=='POST':
        course.delete()
        return redirect('courses')
    context={
        'course':course
    }
    return render(request,'register/deleteCourse.html',context)
def updateCourse(request,pk):
    course=Courses.objects.get(id=pk)
    form=CourseForm(instance=course)
    if request.method=='POST':
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    context={
        "form":form,
        }
    return render(request,'register/courseForm.html',context)