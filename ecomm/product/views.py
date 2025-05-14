from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from category.models import category
from product.models import product

def index(req):
    products = product.objects.all()
    context = {'products':products}
    return render(req, template_name='index.html',context=context)

def new_product(req):
    categories = category.objects.all()
    context = {'categories':categories}
    print(req.FILES.get('image_url'))         # Should be a single UploadedFile
    print(type(req.FILES.get('image_url')))   # Should be <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>

    if req.method == 'POST':
        categoryObj = category.objects.get(pk=req.POST['category'])

        product.objects.create(
            name=req.POST['name'],
            description=req.POST['description'],
            price=req.POST['price'],
            stock=req.POST['stock'],
            image=req.FILES['image_url'],
            sku=req.POST['sku'],
            date_added=req.POST['date_added'],
            categoryobj=categoryObj
        )
        return redirect('index')
    return render(req, template_name='add_product.html',context=context)


def upd_product(req,id):
    pass

def del_product(req,id):
    pass 