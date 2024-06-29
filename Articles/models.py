from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Articles(models.Model):
    title = models.CharField(max_length=50, null=False)
    body = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


    def __str__(self):
        return self.title
    
# Create your models here.
