from django.shortcuts import render
from django.shortcuts import HttpResponse
def musics(request):
    #return HttpResponse('You are looking at musics')
    return render(request, "musics.html")
def first_view(request):
    #return HttpResponse('Welcome to the music documentary')
    return render(request, 'first_view.html')
def articles(request):
    return render(request, 'articles.html')