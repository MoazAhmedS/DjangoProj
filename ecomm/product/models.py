from django.db import models
from category.models import category
# Create your models here.
class product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    image = models.ImageField(upload_to='product_imgs/',blank=True,null=True)
    sku=models.CharField(unique=True,max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)
    categoryobj=models.ForeignKey(category,on_delete=models.CASCADE)
