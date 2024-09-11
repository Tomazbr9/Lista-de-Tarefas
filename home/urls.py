from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('tarefas/<int:id>/', views.task_view, name='task'),
    path('tarefas/<int:id>/delete/', views.delete, name='delete'),
    path('tarefas/<int:id>/update/', views.update, name='update'),
    path('check/<int:id>/', views.checkbox_view, name='checkbox'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
