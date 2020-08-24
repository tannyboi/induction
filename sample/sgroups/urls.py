from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'auth',views.Auth0)
# router.register(r'add_post',views.add_Post)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register', views.register, name='register'),
    path('changename/<name>',views.changename.as_view(),name='namechange'),
    path('group_add/<grp_name>/<admin_name>', views.group_add.as_view(), name='new group'),
    path('UsersList/<name>', views.UsersList.as_view(), name='UsersList'),
    path('GroupsList/<name>', views.GroupsList.as_view(), name='GroupsList'),
    path('AddMembers/<grp_name>/<name>/<role>', views.AddMembers.as_view(), name='Addition'),
    path('ChangePermissions/<grp_name>/<name>/<role>', views.ChangePermissions.as_view(), name='UsersList'),
    path('AddPost', views.AddPost, name='AddPost'),
    path('EditPost/<postid>', views.EditPost, name="edit"),
    path('CheckAll/<grp_name>', views.CheckAll.as_view(), name='Moderation'),
    path('Moderate/<grp_name>/<postid>', views.Moderate.as_view(), name='Approve'),
    path('Delete/<grp_name>/<postid>', views.Delete.as_view(), name='delete'),

]