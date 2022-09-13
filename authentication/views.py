from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import User


def register(request):
    """
    If the request method is POST, then we get the first name, last name, and email from the
    request.POST dictionary.
    If the two passwords match, then we create a new user with the given information and save it to the
    database.
    If the passwords don't match, then we display an error message.
    If the request method is not POST, then we just render the register.html template

    :param request: The request object is a Django object that contains all the information about the
    current request
    """

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        if request.POST["password1"] == request.POST["password2"]:
            password = request.POST["password1"]
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect("register")
            user = User.objects.create_user(
                username=email,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "register.html")


def login(request):
    """
    When the user visits the login page, render the login.html template.
    """
    return render(request, "login.html")


def login_user(request):
    """
    If the request method is POST, then we get the email and password from the
    request.POST dictionary.
    """
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect("application")
    else:
        messages.error(request, "Invalid credentials")
        return redirect("login")


@login_required(login_url="login")
def logout(request):
    """
    It logs out the user and redirects them to the login page.
    :param request: The request is required for authentication and access to session data
    """
    auth_logout(request)
    return redirect("login")
