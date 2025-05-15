from django.db import models
from category.models import category
# Create your models here.
class product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    image = models.ImageField(upload_to='product_imgs/img',blank=True,null=True)
    sku=models.CharField(unique=True,max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)
    categoryobj=models.ForeignKey(category,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

    @classmethod
    def add_product(cls,name,des,price,stock,img,sku,date,catID):
        return cls.objects.create(
            name=name,
            description=des,
            price=price,
            stock=stock,
            image=img,
            sku=sku,
            date_added=date,
            categoryobj=catID
        )
    
    @classmethod
    def get_products(cls):
        return cls.objects.filter(status=True)
    
    @classmethod
    def del_product(cls,id):
        return cls.objects.filter(id=id).update(status=False)