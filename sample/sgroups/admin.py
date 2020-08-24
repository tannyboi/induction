from django.contrib import admin
from .models import MyUser,MyGroup,Post
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(MyGroup)