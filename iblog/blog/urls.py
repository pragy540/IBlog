from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.bloghome, name="bloghome"),
    path('<int:id>/', views.blogpost, name="blogpost"),
    path('signup/', views.handlesignup, name='handlesignup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pr<int:id>/', views.personal, name='personal'),
    path('update<int:id>/', views.update, name='update'),


]
