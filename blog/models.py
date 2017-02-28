from django.db import models
from django.utils import timezone
from django import forms
from django.core.urlresolvers import reverse

def generate_post_name(instance, filename):
    url = "images/posts/{0}_{1}.jpg".format(
        instance.title, instance.author)
    return url


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique=True,null=True)
    image = models.ImageField(upload_to=generate_post_name, null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)   
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0) #models.TimeField(null=True, blank=True) #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)

    def approved_comments(self):
        return  self.comments.filter(approved_comment=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',  related_name='comments')
    author =  models.CharField(max_length=200)
    text  =  models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return  self.text