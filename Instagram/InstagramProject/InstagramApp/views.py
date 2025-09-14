from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'InstagramHtml/main.html')

def login(request):
    return render(request, 'InstagramHtml/login.html')

def signup(request):
    return render(request, 'InstagramHtml/signup.html')

def profile(request):
    return render(request, 'InstagramHtml/profile.html')

#def post(request):
#    return render(request, 'InstagramHtml/post.html')

# def explore(request):
#     return render(request, 'InstagramHtml/explore.html')  

#def like(request):
#    return render(request, 'InstagramHtml/like.html')

#def comments(request):
#    return render(request, 'InstagramHtml/comments.html')

#def explore(request):
#    return render(request, 'InstagramHtml/explore.html')

