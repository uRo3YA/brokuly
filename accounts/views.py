from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def test(request):
    return render(request, 'accounts/test.html')


def agreement(request):
    context = {
        'buyer': 0,
        'seller': 1, 
    }

    return render(request, 'accounts/agreement.html', context)


def signup(request, is_seller):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save(commit=False).is_seller = is_seller
            form.save()

            # must change this statement
            return render(request, 'accounts/test.html')

    else:
        form = CustomUserCreationForm()
        
        # Hide address part of the form
        if is_seller:
            form.fields['address'].widget = forms.HiddenInput()

    context = {
        'form': form
    }

    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            # must change this statement
            return redirect(request.GET.get('next') or 'accounts:test')

    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }

    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)

    # must change this statement
    return redirect('accounts:login')