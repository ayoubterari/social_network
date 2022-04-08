from django.contrib import admin
from .models import Post, UserProfile, Comment, ThreadModel

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(ThreadModel)