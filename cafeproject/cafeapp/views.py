from django.shortcuts import render


def HomeView(requests):
    return render(requests, 'cafeapp/index.html')