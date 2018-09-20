from django.shortcuts import render
from .models import Show, Cast, Circle


def main(request):
    shows = Show.objects.all()
    circles = Circle.objects.all()
    return render(request, 'petter.html', {'shows': shows, 'circles': circles})
