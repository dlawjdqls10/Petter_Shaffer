from django.shortcuts import render
from .models import Show, Cast, Circle


def main(request):
    return render(request, 'petter.html')
