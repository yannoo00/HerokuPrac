from django.shortcuts import render

# Create your views here.

def heroku(request):
    return render(request, 'heroku.html')