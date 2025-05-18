from django.db import models

# Create your models here.
class category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()

    @classmethod
    def getAll(cls):
        return cls.objects.all()
    
    def __str__(self):
        return self.name