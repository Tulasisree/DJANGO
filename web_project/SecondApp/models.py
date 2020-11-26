from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    age = models.IntegerField()
    phone = models.CharField(null=True,blank=True,max_length=10)
    def __str__(self):
       return self.name

