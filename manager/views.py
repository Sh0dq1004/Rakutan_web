from django.shortcuts import render
from . import forms
from .models import tire1_class, tire2_class

import csv

# Create your views here.
def admin_template(request):
    if (request.method=="POST"):
        if "dbsort" in request.POST:
            with open("tire1.csv", "r", encoding="utf-8") as f:
                reader=csv.reader(f)
                rows=[]
                for i in reader:
                    rows.append(i)
                for row in rows:
                    tire1_class.objects.create(
                        name=row[0],
                        teaher=row[1],
                        term=row[2]
                    )
            with open("tire2.csv", "r", encoding="utf-8") as f:
                reader=csv.reader(f)
                rows=[]
                for i in reader:
                    rows.append(i)
                for row in rows:
                    tire2_class.objects.create(
                        name=row[0].replace("\u3000",' '),
                        teaher=row[1].replace("\u3000",' '),
                        term=row[2].replace("\u3000",' '),
                        grade=row[3].replace("\u3000",' '),
                        major=row[4].replace("\u3000",' ')
                    )
    return render(request, 'admin.html')

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