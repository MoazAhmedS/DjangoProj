from django.urls import path
from django.urls import include
from product.views import *
from .api.views import *


urlpatterns = [

    path('API/Class/<int:id>', ProductUpdateView.as_view()),
    
    #function based views Create/List
    path('API/', product_list_create),


    path('new/',new_product,name='n_product'),
    path('update/<int:id>/',upd_product,name='u_product'),
    path('product/<int:id>/',product_detail,name='det_product'),
    path('delete/<int:id>/',Del_product_v.as_view(),name='d_product'),
]