from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    surname = models.CharField(max_length=20, verbose_name='Surname')

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        
        return reverse('blog:detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('blog:update', kwargs={'id': self.id})

