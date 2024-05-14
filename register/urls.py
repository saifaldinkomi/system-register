from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name='home'),
    path('courses/',views.courses,name='courses'),
    path('coursesSchduels/',views.coursesSchedules, name='coursesSchedules'),
    path('students/',views.students,name='students'),
    path('studentsReg/',views.studentsReg,name='studentsReg'),
    path('create/',views.create,name='create'),
    path('userLogin/',views.userLogin,name='login'),
    
]
