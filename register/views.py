from django.shortcuts import render,redirect
from .forms  import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.contrib import messages
from .filters import *
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, render


@login_required(login_url='login')
def main(request):
    courses=Courses.objects.all() 
    searchFilter=CourseFilter(request.POST,queryset=courses)
    courses=searchFilter.qs
    context={
        'courses':courses,
        'searchFilter':searchFilter
    }
    return render(request,"register/main.html",context)


@login_required(login_url='login')
def courses(request):
    courses=Courses.objects.all() 
    searchFilter=CourseFilter(request.POST,queryset=courses)
    courses=searchFilter.qs
    
    context={
        'courses':courses,
        'searchFilter':searchFilter,
    }
    return render(request,"register/courses.html",context)
@login_required(login_url='login')
def news(request):
    news=News.objects.all()
    context={
        "news":news
    }
    return render(request,"register/news.html",context)

@login_required(login_url='login')
def view(request, pk):
    course = get_object_or_404(Courses, id=pk)
    studentReg = StudentsReg.objects.filter(courseId=course).count()
    context = {
        'course': course,
        'studentReg':studentReg
    }
    return render(request, 'register/view.html', context)
   

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
def studentsReg(request,pk):
    student = Students.objects.get(id=pk)
    registrations = StudentsReg.objects.filter(studentId=pk)
    courses = []
    for reg in registrations:
        course = reg.courseId
        if course and course.scheduleId:
            courses.append({
                'name': course.name,
                'description': course.description,
                'instructor': course.instructor,
                'roomNo': course.scheduleId.roomNo,
                'days': ', '.join([day.name for day in course.scheduleId.days.all()]),
                'startTime': course.scheduleId.startTime.strftime('%H:%M'),
                'endTime': course.scheduleId.endTime.strftime('%H:%M')
            })
    context = {
        'student_name': student,
        'courses': courses
    }
    return render(request, 'register/studentsReg.html', context)

 
def create(request):
    form=createNewUser()
    if request.method=='POST':
        form=createNewUser(request.POST)
        if form.is_valid():  
            user=form.save(commit=False)
            user.password = make_password(form.cleaned_data['password']) 
            form.save()
            return redirect('login')
    else:
       form=createNewUser()
    return render(request,'register/create.html',{'form': form})


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('news')
        else:
            messages.error(request, "Invalid username or password.")
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
def register_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    student = request.user.student  
    if StudentsReg.objects.filter(studentId=student, courseId=course).exists():
        return render(request, 'register/studentsReg.html')
    registration = StudentsReg(studentId=student, courseId=course)
    registration.save()
    return render(request, 'register/studentsReg.html')

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


