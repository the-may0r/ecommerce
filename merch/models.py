from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Merch(models.Model):
    category = models.ForeignKey(Category, related_name='Merches', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='Merch_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='Merches', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Merches'
    
    def __str__(self):
        return self.name
