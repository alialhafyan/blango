from django.db import models
from django.contrib.auth.models import User
# Create your models here 

class Tag(models.Model):
  value = models.TextField(max_length=100, unique=True)
  def __str__(self):
    return self.value
class Comment(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=1000)
    modified_at=models.DateTimeField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    modified_at=models.DateTimeField(null=True)
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at  = models.DateTimeField(auto_now=True)   
    published_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=255) 
    slug = models.SlugField(unique=True)  
    summary = models.TextField(max_length=1000)  
    content=models.TextField(max_length=3000)
    tags = models.ManyToManyField(Tag, related_name='posts')
    comments=models.ManyToManyField(Comment,related_name="comment")
