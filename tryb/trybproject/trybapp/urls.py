from django.urls import path
from trybapp import views

urlpatterns = [
    path('',views.Homepage,name='home'),
    path('register/',views.Registerpage,name='register'),
    path('login/',views.Loginpage,name='login'),
]