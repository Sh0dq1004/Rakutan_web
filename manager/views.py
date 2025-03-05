from django.shortcuts import render

# Create your views here.
def init_template(request):
    return render(request, 'init.html')

def home_template(request):
    return render(request, 'home.html')

def more_template(request):
    return render(request, 'more.html')