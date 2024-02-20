from django.http import HttpResponse
from django.shortcuts import render

from .models import Movie


def home(request):
    """A simple homepage."""
    search_term = request.GET.get('searchMovie')
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    return render(
        request, 'home.html',
        {'searchTerm': search_term, 'movies': movies})


def about(request):
    """An simple about page."""
    return HttpResponse('<h1>Welcome to About Page</h1>')


def signup(request):
    """A simple signup page."""
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
