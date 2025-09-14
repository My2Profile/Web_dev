from django.shortcuts import render
from .models import Movie
from .fovorms import GenreForm

# Create your views here.


def movies_list(request):

	movies = Movie.objects.all()

	return render(request, 'movies/templates/movies/movie_list.html', { 'movies': movies })



def movie_detail(request, pk):

	movie_detail = get_object_or_404(Movie, pk=pk)

	render(request, 'movie_detail.html', { 'movie_details' : movie_details})




def add_genre(request):

	if request.method = 'GET':
		form = GenreForm()
	else:
		form = GenreForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect("templates/movie_list.html")


	return render(request, 'templates/movies/add_genre.html', {'movies' : movies})