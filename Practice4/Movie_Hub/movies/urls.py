from django.urls import path
from . import views

urlpatterns = [
	
	path('/', views.movies_list, name='movies_list'),

	path('/movies/<pk>/', views.movie_detail, name='movie_detail'),



]