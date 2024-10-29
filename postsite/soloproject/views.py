from django.shortcuts import render



def soloproject(request):
    return render(request,'blog/index.html')

def index(request):
    return render(request, 'blog/index.html')

def farmer(request):
    return render(request, 'blog/farmer.html')

def login(request):
    return render(request, 'blog/login.html')

def semipage(request):
    return render(request, 'blog/semipage.html')

def solo(request):
    return render(request, 'blog/solo.html')