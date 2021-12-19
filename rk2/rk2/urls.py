"""rk2 URL Configuration

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
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('book/', include([
        path('', views.read_book, name='read_book'),
        path('create/', views.create_book, name="create_book"),
        path('update/<int:book_id>/', views.update_book, name="update_book"),
        path('delete/<int:book_id>/', views.delete_book, name="delete_book"),
    ])),
    path('library/', include([
        path('', views.read_library, name='read_library'),
        path('create/', views.create_library, name="create_library"),
        path('update/<int:library_id>/',
             views.update_library, name="update_library"),
        path('delete/<int:library_id>/',
             views.delete_library, name="delete_library"),
    ])),
    path('report/', views.report, name="report"),
]
