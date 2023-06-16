from login import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('createForm/', views.createForm),
    path('info/', views.info),
    path('login', views.login),
    path('addForm/', views.addForm),
    path('hr/', views.hr),
    path('leader/', views.leader),
    path('logout', views.logout),
]