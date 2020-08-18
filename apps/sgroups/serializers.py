from rest_framework import serializers
from .models import MyUser,MyGroup,Post
#Create your serializers here

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('name','userid','number','email',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyGroup
        fields = ('name', 'groupid','users','size')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'content','postid','createdon')

