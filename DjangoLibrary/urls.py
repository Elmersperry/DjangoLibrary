"""
URL configuration for DjangoLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from library.views import index, add_author, add_book, show_all_authors, show_all_books

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('author_list/', show_all_authors, name='author_list'),
    path('author/', add_author, name='add_author'),
    path('book_list/', show_all_books, name='book_list'),
    path('book/', add_book, name='add_book'),
]