from django.contrib import admin
from .models import Post, Like, Comment, Friendship, UserProfile
# Register all models
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Friendship)
admin.site.register(UserProfile)
