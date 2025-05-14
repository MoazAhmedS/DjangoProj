"""
URL configuration for ecomm project.

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
from category.views import *
from product.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('product/new/',new_product,name='n_product'),
    path('product/update/<int:id>/',upd_product,name='u_product'),
    path('product/delete/<int:id>/',del_product,name='d_product'),
    path('category/',v_categ,name='v_categ'),
    path('category/new/',new_categ,name='n_categ'),
    path('category/update/<int:id>/',upd_categ,name='u_categ'),
    path('category/delete/<int:id>/',del_categ,name='d_categ'),
    
]
