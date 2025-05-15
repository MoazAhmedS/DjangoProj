from django.urls import path
from django.urls import include
from product.views import *

urlpatterns = [
    path('new/',new_product,name='n_product'),
    path('update/<int:id>/',upd_product,name='u_product'),
    path('delete/<int:id>/',del_product,name='d_product'),
]