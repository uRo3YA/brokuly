from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django import forms


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

    return render(request, 'accounts/signup.html', context)