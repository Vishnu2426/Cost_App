from django.shortcuts import render

def index(request):
    print("hello","Base view accessed") 
    return render(request, 'index.html') 