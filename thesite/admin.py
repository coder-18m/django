from django.contrib import admin
from .models import Post, Category, Profile, Comment, Place, MailMessage, Subscribers

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Place)
admin.site.register(MailMessage)
admin.site.register(Subscribers)
