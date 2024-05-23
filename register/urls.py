from django.urls import path
from . import views
urlpatterns = [
    # path('',views.main,name='home'),
    path('courses/',views.courses,name='courses'),
    path('coursesSchduels/',views.coursesSchedules, name='coursesSchedules'),
    path('students/',views.students,name='students'),
    path('studentsReg/<str:pk>',views.studentsReg,name='studentsReg'),
    path('create/',views.create,name='create'),
    path('userLogin/',views.userLogin,name='login'),
    path('createCourse/',views.createCourse,name='createCourse'),
    # path('createSchedules/',views.createSchedules,name='createSchedules'),
    path('deleteCourse/<str:pk>',views.deleteCourse,name='deleteCourse'),
    path('updateCourse/<str:pk>',views.updateCourse,name='updateCourse'),
    path('userLogout/',views.userLogout,name='userLogout'),
    path('profile/',views.profile,name='profile'),
    path('view/<int:pk>',views.view,name='view'),
    path('register_course/<int:course_id>',views.register_course,name='register_course'),
    path('',views.news,name='news'),
    #  path('registerCourse/<str:pk>',views.registerCourse,name='registerCourse'),
    #  path('studentSchedule/',views.studentSchedule,name='studentSchedule'),
]
