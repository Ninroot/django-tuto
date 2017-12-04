from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


# @login_required
def home(request):
    return render(request, 'core/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # save the user in the database
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            signin(request, user)
            return HttpResponseRedirect(reverse('core:home'))
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


# The loggin function is already defined by django
def signin(request, user=None):
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('core:home'))

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('core:home'))
        else:
            return render(request, 'core/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'core/signin.html', {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:home'))
