"""todo_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from todo_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # View solution 1
    #path('', views.home, name='home'),
    #path('todo/<int:id>/', views.todo_detail, name='todo_detail'),

    # View soluton 3
    path('users/', views.ListUsers.as_view()),
    path('todo_list/', views.ToDoListView.as_view()),
    path('todo/<str:task>', views.ToDoViewDefault.as_view()),
    path('todo_info/<str:task>', views.ToDoView.as_view()),
    path('todo/', views.ToDoListViewDefault.as_view()),
    path('todo_list/', views.ToDoListView.as_view()),

    # View solution 2, (Viewset)
    path('', include('todo_app.urls')),

]
