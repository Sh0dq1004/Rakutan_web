from django.shortcuts import render
from . import forms

# Create your views here.
def init_template(request):
    major_grade_form=forms.major_grade_select()
    context={
        'form':major_grade_form
    }
    if (request.method=="POST"):
        print(request.POST["choices"])

    return render(request, 'init.html',context=context)

def home_template(request):
    return render(request, 'home.html')

def more_template(request):
    return render(request, 'more.html')