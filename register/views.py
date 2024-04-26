from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    return render(request,"register/main.html")
def courses(request):
    return render(request,"register/courses.html")
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