from django.shortcuts import render
from django.http import HttpResponse

posts = [
 {'author' : 'Sharanya Warrier',
   'title' : ' Mahamantra',
   'content' : ' Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare',
   'date_posted' : 'August 27, 2018'

 }
]


def home (request):
    return render(request, 'blog2/home.html' )

def about (request):
    return render(request, 'blog2/about.html')

def contact (request):
    return HttpResponse('<h1> Contact Details </h1>')

def stores (request):
    return HttpResponse('<h1> STORE DETAILS </h1>')
