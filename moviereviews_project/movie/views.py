from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """A simple homepage."""
    search_term = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm': search_term})


def about(request):
    """An simple about page."""
    return HttpResponse('<h1>Welcome to About Page</h1>')


def signup(request):
    """A simple signup page."""
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
