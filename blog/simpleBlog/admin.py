from django.contrib import admin
from simpleBlog.models import Post
from simpleBlog.models import Comment

class CommentAdmin(admin.StackedInline):
	model = Comment

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['content']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [CommentAdmin]
admin.site.register(Post, PostAdmin)