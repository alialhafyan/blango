from django.db import models

# Create your models here 

class Tag(models.Model):
  value = models.TextField(max_length=100, unique=True)
  def __str__(self):
    return self.value
class Post(models.Model):
    author_id = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at  = models.DateTimeField(auto_now=True)   
    published_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=255) 
    slug = models.SlugField(unique=True)  
    summary = models.TextField(max_length=1000)  
    content=models.TextField(max_length=3000)
    tags = models.ManyToManyField(Tag, related_name='posts')

