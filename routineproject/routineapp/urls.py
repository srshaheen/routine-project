from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('home/', views.DashBoard, name='home'),
    path('all-courses/', views.AllCourses, name='all_courses'),
]
