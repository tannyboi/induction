from django.db import models
from django.contrib.auth.models import User,Group
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(unique=True, max_length=500)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=13,unique=True)
    userid = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return "user {} is {} ".format(self.name,self.userid)


class MyGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, )
    size = models.IntegerField(default=1)
    groupid = models.AutoField(primary_key=True)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "group {} is {}".format(self.name, self.groupid)


class Post(models.Model):
        content = models.TextField()
        createdon = models.DateTimeField(auto_now_add=True)
        user = models.ForeignKey(to=User, on_delete=models.CASCADE)
        postid = models.AutoField(primary_key=True)

        class Meta:
            ordering = ['content','createdon']

        def __str__(self):
            return "Post {} is {}".format(self.content,self.postid)

        def CreatePost(User, self):
            self.author = User

        def EditPost(self):
            self.content = models.TextField()

        def DeletePost(self):
            del self