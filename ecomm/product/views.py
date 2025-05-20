from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from category.models import category
from product.models import product
from .forms import *
import os
from django.views import View

class Index(View):
    def get(self,request):
        context = {'products': product.get_products()}
        return render(request, 'index.html', context)

class Del_product_v(View):
    def get(self,request,id):
        product.del_product(id)
        return redirect('index')

def product_detail(req,id):
    context = {}
    context = {'product':product.objects.get(pk=id)}
    return render(req, 'product.html', context)

def new_product(req):
    context = InsertProductForm()
    context = {'form':context}
    if req.method == 'POST':
        form = InsertProductForm(data=req.POST, files=req.FILES)
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('index')
    return render(req, template_name='add_product.html', context=context)


def upd_product(req,id):
    oldPro=product.objects.get(pk=id)
    initail_data={
        'name': oldPro.name,
        'description': oldPro.description,
        'price':oldPro.price,
        'categoryobj':oldPro.categoryobj.id
    }
    context={'form':UpdateProductForm(initial=initail_data),'product_image':oldPro.image.url}
    if req.method=='POST':
        form=UpdateProductForm(data=req.POST,files=req.FILES,initial=initail_data)
        if form.is_bound and form.is_valid():
            oldPro.name=form.cleaned_data['name']
            oldPro.description=form.cleaned_data['description']
            oldPro.price=form.cleaned_data['price']
            if form.cleaned_data['image']:
                if os.path.exists(oldPro.image.path):
                    os.remove(oldPro.image.path)
                oldPro.image = form.cleaned_data['image']
            oldPro.categoryobj=category.objects.get(pk=form.cleaned_data['categoryobj'])
            oldPro.save()
            return redirect('index')
        else:
            context['msg']=form.errors
    return render(req, 'update_product.html', context)


def del_product(req,id):
    product.del_product(id)
    return redirect('index')

