from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error (request, "The passwords do not match. Please try again.")
            return render (request, "signup.html")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already in use. Please try again.")
            return render (request, "signup.html")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use. Please try again.")
            return render (request, "signup.html")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # The user is sent back to home page upon successful sign-up.
        login(request, user)
        return redirect("home")
    
    return render (request, "home.html")