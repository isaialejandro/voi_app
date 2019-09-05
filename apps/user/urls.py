from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, User

from django.urls import path, include

from apps.user.views import UserList, CreateUser, UpdateUser#, PermissionsList, CreatePermission, UpdatePermission, DeletePermission, \
							#ProfileList, CreateProfile, UpdateProfile, DeleteProfile


urlpatterns = [
	path('list/', UserList.as_view(), name='list'),
	path('new/', CreateUser.as_view(), name='new'),
	path('update/<int:pk>', UpdateUser.as_view(), name='update_user'), #update & disable user.

	
]

"""
	path('permissions/', PermissionsList.as_view(), name='permissions'),
	path('create/', CreatePermission.as_view(), name='permissions'),
	path('update/<int:pk>', UpdatePermission.as_view(), name='create_permission'),
	path('delete_permission/', DeletePermission.as_view(), name='delete_permission'),

	path('list/', ProfileList.as_view(), name='profiles'),
	path('create/', CreateProfile.as_view(), name='create_profile'),
	path('update/<int:pk>', UpdateProfile.as_view(), name='update_profile'),
	path('delete/<int:pk>', DeleteProfile.as_view(), name='delete_profile'),
	"""