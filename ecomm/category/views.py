from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import category

class CatListView(ListView):
    model = category
    template_name = 'category_list.html'

class CatCreateView(CreateView):
    model = category
    fields = ['name', 'description']
    template_name = 'add_categ.html'
    success_url = reverse_lazy('category_list')

class CatUpdateView(UpdateView):
    model = category
    fields = ['name', 'description']
    template_name = 'add_categ.html'
    success_url = reverse_lazy('category_list')

class CatDeleteView(DeleteView):
    model = category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
