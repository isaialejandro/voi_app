from django.shortcuts import render

from django.contrib.auth.models import Permission, User

from django.views.generic import View


class UserList(View):

	def get(self, request):

		u_list = User.objects.all().exclude(username='Pending')

		context = {}
		context['user_list'] = True
		context['u_list'] = u_list

		return render(request, 'user_list.html', context)


class CreateUser(View):

	def get(self, request):

		context = {}
		context['create_user'] = True
		return render(request, 'list.html', context)


class UpdateUser(View):

	def get(self, request, *args):

		context = {}
		context['update_user'] = True
		return render(request, 'list.html', context)