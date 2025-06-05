from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    """
    Render the home page of the book catalog.
    """
    return HttpResponse("Welcome to the Book Catalog!")   
