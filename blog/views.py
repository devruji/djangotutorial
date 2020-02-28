from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Post
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    # [Query data from Models]
    data = Post.objects.all()
    return render(request, 'index.html', {'posts': data})


def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cfpassword = request.POST['cfpassword']

        # [CREATE USER]
        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
        )

        # [SAVE USER]
        user.save()

        return render(request, 'results.html')
    return render(request, 'form.html')
