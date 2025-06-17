from django.db import models

# Create your models here.



class employee(models.Model):
    idd=models.CharField(max_length=12)
    name=models.CharField(max_length=200)
    contact=models.IntegerField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.name
    
    
