from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class  Category(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')  

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    category = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home') 

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    body = models.TextField()      
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)
    
