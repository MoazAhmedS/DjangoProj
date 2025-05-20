from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import category

class CategoryListView(ListView):
    model = category
    template_name = 'category_list.html'

class CategoryCreateView(CreateView):
    model = category
    fields = ['name', 'description']
    template_name = 'add_categ.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = category
    fields = ['name', 'description']
    template_name = 'add_categ.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
