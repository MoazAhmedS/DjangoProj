from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from category.models import category
from product.models import product

def index(req):
    products = product.get_products()
    context = {'products':products}
    return render(req, template_name='index.html',context=context)

def new_product(req):
    categories = category.getAll()
    context = {'categories':categories}

    if req.method == 'POST':
        categoryObj = category.objects.get(pk=req.POST['category'])

        product.add_product(
            name=req.POST['name'],
            des=req.POST['description'],
            price=req.POST['price'],
            stock=req.POST['stock'],
            img=req.FILES['image_url'],
            sku=req.POST['sku'],
            date=req.POST['date_added'],
            catID=categoryObj
        )
        return redirect('index')
    return render(req, template_name='add_product.html',context=context)



def upd_product(req,id):
    pass

def del_product(req,id):
    product.del_product(id)
    return redirect('index')

