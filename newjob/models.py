from django.db import models

# Create your models here.

class Newjob(models.Model):
    title = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=100, null=False)
    background = models.TextField()
    price = models.DecimalField(max_digits= 15, decimal_places=3, null=False)
    image = models.ImageField(upload_to='static/newjob/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)