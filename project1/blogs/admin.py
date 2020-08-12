from django.contrib import admin
from .models import Post,Comment
# Register your models here.

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post','created_on','active')
    list_filter = ('active','created_on')
    search_fields = ('name', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

#admin.site.register(Post,Comment)
#admin.site.register(PostAdmin)