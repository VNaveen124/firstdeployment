# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    logout(request)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))
    return HttpResponseRedirect(reverse('myapp:index'))

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)
        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            #return HttpResponseRedirect(reverse('myapp:index'))
            return HttpResponseRedirect(reverse('myapp:index'))
        # Otherwise, return login page again with new context
        else:
            return render(request, "user_auth/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "user_auth/login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        if User.objects.create_user(username, email, password):
         return HttpResponseRedirect(reverse("user_auth:login"))
        else:
            #exception to be handled
            return HttpResponse('user already existed')


    return render(request, "user_auth/signup.html")
