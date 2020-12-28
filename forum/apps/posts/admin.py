from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text', )

class CommentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'text', 'post', 'author')
    list_display_links = ('id', 'text', 'post')
    list_filter = ('post', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)