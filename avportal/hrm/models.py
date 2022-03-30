from django.db import models

# Create your models here.

class Detail(models.Model):
    project_choice= (
        ('RD', 'roadhow'),
        ('CL', 'clara'),
        ('AV', 'avdevs'),
        ('SA', 'streetai'),
        ('9F', '9tofive'),
        )
    emp_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50 , default ="default value")
    last_name = models.CharField(max_length=50, default ="default value")
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    photos = models.ImageField(upload_to='photos/emp')
    
    project = models.CharField(choices = project_choice,max_length=100, default ="default value")
    

   
    def __str__(self):
        return self.first_name
