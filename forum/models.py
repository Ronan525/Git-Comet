from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts')
    
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='draft')