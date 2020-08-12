from django.contrib import admin
from .models import details,edu_history

# Register your models here.
'''
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    headliner = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    coreinterest = models.CharField(max_length=100)
    secondary_interest = models.CharField(max_length=100)
    last_interest = models.CharField(max_length=100)
    
    details = models.ForeignKey(details,on_delete=models.CASCADE,related_name='comments')
    percentage = models.CharField(max_length=5,unique=False)
    institution = models.CharField(max_length=250, unique=False)
    subject = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'comment {} for {}'.format(self.description,self.details)
'''
@admin.register(details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('author', 'updated_on', 'headliner',)
    list_filter = ("coreinterest",)
    search_fields = ['coreinterest', 'secondary_interest','last_interest']
    #prepopulated_fields = {'slug': ('title',)}

@admin.register(edu_history)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('institution', 'subject', 'percentage','created_on',)
    list_filter = ('created_on',)
    search_fields = ('subject', )
    #actions = ['approve_comments']

    #def approve_comments(self, request, queryset):
     #   queryset.update(active=True)