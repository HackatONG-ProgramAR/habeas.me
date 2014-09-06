from django.shortcuts import render
from .forms import SearchForm


def home(request):
    form = SearchForm()
    context = { 'form' : form }
    return render(request, 'index.html', context)
