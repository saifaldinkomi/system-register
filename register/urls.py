from django.urls import path
from . import views
urlpatterns = [
    path('',views.main),
    path('courses/',views.courses),
    path('coursesSchduels/',views.coursesSchedules),
    path('students/',views.students),
    path('studentsReg/',views.studentsReg),
]
