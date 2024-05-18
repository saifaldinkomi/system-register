from django.shortcuts import render,redirect
from .forms  import *
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.contrib import messages
from .filters import *
from django.contrib.auth.decorators import login_required
from .decorators import *
@login_required(login_url='login')

def main(request):
    return render(request,"register/main.html")
@login_required(login_url='login')

def courses(request):
    courses=Courses.objects.all() 
    searchFilter=CourseFilter(request.POST,queryset=courses)
    courses=searchFilter.qs
    context={
        'courses':courses,
        'searchFilter':searchFilter
    }
    return render(request,"register/courses.html",context)
@login_required(login_url='login')
def coursesSchedules(request):
    return render(request,"register/coursesSchedules.html")
@login_required(login_url='login')
def students(request):
    student=Students.objects.all()
    context={
        "student":student,
    }
    return render(request,"register/students.html",context)
@login_required(login_url='login')
def studentsReg(request):
    studentsReg=StudentsReg.objects.all()
    context={
        'studentsReg':studentsReg
    }
    return render(request,"register/studentsReg.html",context)
@notLogUser
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
@notLogUser
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user=auth.authenticate( username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            
    return render(request, 'register/login.html')
@login_required(login_url='login')
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
@login_required(login_url='login')
def createSchedules(request):
    form=SchedulesForm()
    if request.method=='POST':
        form=SchedulesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createCourse')
    context={
        'form':form
    }
    return render(request,'register/scheduleForm.html',context)
@login_required(login_url='login')
def deleteCourse(request,pk):
    course=Courses.objects.get(id=pk)
    if request.method=='POST':
        course.delete()
        return redirect('courses')
    context={
        'course':course
    }
    return render(request,'register/deleteCourse.html',context)
@login_required(login_url='login')
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
@login_required(login_url='login')  
def userLogout(request):
    logout(request)
    return redirect ('login')
@login_required(login_url='login')  
@allowedUsers
def profile(request):
    return render(request,'register/profile.html')
    