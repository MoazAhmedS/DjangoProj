from django.urls import path
from django.urls import include
from category.views import *
from .views import CatListView, CatCreateView, CatUpdateView, CatDeleteView

urlpatterns = [
    path('',CatListView.as_view(),name='category_list'),
    path('new/',CatCreateView.as_view(),name='category_add'),
    path('update/<int:pk>/',CatUpdateView.as_view(),name='category_edit'),
    path('delete/<int:pk>/',CatDeleteView.as_view(),name='category_delete'),
]