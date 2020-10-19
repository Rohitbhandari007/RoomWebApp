from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    
    title = models.CharField(max_length=100)
    description =models.TextField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField(default=False)
    price=models.TextField(default=False)
    image=models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title