from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from .forms import GenreForm, LoginForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.  
def home_page(request):
    """
    Render the home page of the book catalog.
    """
    return HttpResponse("Welcome to the Book Catalog!")   



def book_list(request):

    books = Book.objects.all()

    return render(request, 'books/book_list.html', {'books' : books})
    


def book_detail(request, pk):

    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/book_detail.html', {'book': book})


def add_genre(request):

    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            form = GenreForm()
        return render(request, 'books/add_genre.html', {'form':form})





def sign_up(request):

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form })



def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', { 'form' : form })
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'users/login.html', {'form': form})
        else:
            return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def secret_author_dashboard(request):
    return HttpResponse(f"Welcome to the Author Dashboard, {request.user.username}!")

