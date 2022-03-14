from django.db import models
# Create your models here.

class Emp(models.Model):
    emp_id= models.CharField(max_length=50, unique=True)
    emp_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/emp')
    project = models.CharField(max_length=50)
    

   
    def __str__(self):
        return self.emp_name