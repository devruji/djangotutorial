from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post

# Create your views here.


def index(request):
    """
        Home page
    """
    # [Query data from Models]
    data = Post.objects.all()
    return render(request, 'index.html', {'posts': data})


def form(request):
    """
        create form for add User
    """
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cfpassword = request.POST['cfpassword']

        if password == cfpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists.')
                return redirect('/form')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists.')
                return redirect('/form')
            else:
                # [CREATE USER]
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=fname,
                    last_name=lname
                )

                # [SAVE USER]
                user.save()
                return redirect('/')

        else:
            messages.info(request, 'Password not match !')
            return render(request, 'form.html')

    return redirect('/')


def login(request):
    """
        get request from login
    """
    username = request.POST['username']
    password = request.POST['password']

    # [LOGIN PROCESS]
    user = auth.authenticate(username=username,
                             password=password)

    # [CHK USER, PWD in Database]
    if user is not None:  # result OK
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'User not found !')
        return redirect('/loginForm')


def logout(request):
    auth.logout(request)
    return redirect('/')


def loginForm(request):
    """
        create form for login
    """
    return render(request, 'login.html')
