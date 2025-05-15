from django.urls import path
from django.urls import include
from category.views import *

urlpatterns = [
    path('/new/',new_categ,name='n_categ'),
    path('/update/<int:id>/',upd_categ,name='u_categ'),
    path('/delete/<int:id>/',del_categ,name='d_categ'),
    
]