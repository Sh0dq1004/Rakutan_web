from django.shortcuts import render
from . import forms

# Create your views here.
def init_template(request):
    major_form=forms.major_select()
    grade_form=forms.grade_select()
    context={
        'major_form':major_form
    }
    if (request.method=="POST"):
        print(request.POST["choices"])

    return render(request, 'init.html',context=context)

def home_template(request):
    return render(request, 'home.html')

def more_template(request):
    return render(request, 'more.html')