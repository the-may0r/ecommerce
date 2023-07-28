from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from merch.models import Category, Merch
from .forms import SignUpForm

# Create your views here


def index(request):
        items = Merch.objects.filter(is_sold=False) [0:6]
        categories = Category.objects.all()
        return render(request, 'index.html', {
            'categories': categories,
            'items': items,
            })

def contact(request):
    return render(request, 'contact.html',{})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {
        'form':form
    })