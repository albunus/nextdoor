from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User

# cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

