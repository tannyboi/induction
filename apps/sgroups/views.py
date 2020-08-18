from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import UserSerializer,GroupSerializer,PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import MyUser,MyGroup,Post
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
#from django.contrib.auth.models import User,Group
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all().order_by('userid')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = MyGroup.objects.all().order_by('groupid')
    serializer_class = GroupSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('postid')
    serializer_class = PostSerializer

def index(request):
    return render(request, '/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            m1 = MyUser.objects.create(user=user,email=username,name="",number=0)
            m1.save()
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()


    context ={'form': form}
    return render(request,'registration/register.htm',context)





