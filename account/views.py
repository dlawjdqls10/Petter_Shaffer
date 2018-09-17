from django.shortcuts import render


def main(request):
    return render(request, 'petter:main')
