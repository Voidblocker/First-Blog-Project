from django.db import models
from django.utils import timezone

# Create your models here.
class  Category(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Post(models.Model):
    title=models.CharField(max_length=100)
    article=models.TextField()
    create_at=models.DateField(auto_now_add=True)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE , null=True, blank=True)
    name=models.CharField(max_length=40, blank=True)
    email=models.EmailField(max_length=254, blank=True)
    comment=models.TextField(blank=True)
    timestamp=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
