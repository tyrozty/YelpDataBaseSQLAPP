from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import YelpData


def index(request):
	return HttpResponse("Hello, world. You're at the YelpData index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'YelpData/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'YelpData/home.html'

class UserListView(generic.ListView):
	model = YelpData
	context_object_name = 'uer'
	template_name = 'YelpData/user.html'
	paginate_by = 50

	def get_queryset(self):
		return # TODO write ORM code to retrieve all Heritage Sites

class UserDetailView(generic.DetailView):
	model = YelpData
	context_object_name = 'user'
	template_name = # TODO add the correct template string value
