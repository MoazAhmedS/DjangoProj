from django.urls import path
from django.urls import include
from category.views import *
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('',CategoryListView.as_view(),name='category_list'),
    path('new/',CategoryCreateView.as_view(),name='category_add'),
    path('/update/<int:pk>/',CategoryUpdateView.as_view(),name='category_edit'),
    path('/delete/<int:pk>/',CategoryDeleteView.as_view(),name='category_delete'),
    
]