from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from category.models import category
# Create your views here.
def v_categ(req):
    pass

def new_categ(req):
    if req.method == 'POST':
        category.objects.create(
            name=req.POST['name'],
            description=req.POST['description'],
        )
        return redirect('index')
    return render(req, template_name='add_categ.html')

def upd_categ(req,id):
    pass

def del_categ(req,id):
    pass 