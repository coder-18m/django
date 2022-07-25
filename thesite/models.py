from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Place(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True,)
    first_name = models.CharField(max_length=255, null=True, blank=True,)
    last_name = models.CharField(max_length=255, null=True, blank=True,)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('edit_profile')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null =True, blank=True, upload_to="images/profile")
    website_url = models.CharField(max_length=255, null=True, blank=True,)
    facebook_url= models.CharField(max_length=255, null=True, blank=True,)
    instagram_url = models.CharField(max_length=255, null=True, blank=True,)
    twitter_url = models.CharField(max_length=255, null=True, blank=True,)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null =True, blank=True, upload_to="images/")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = RichTextField(blank=True, null=True)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title
