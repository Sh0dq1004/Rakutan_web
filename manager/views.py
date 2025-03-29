from django.shortcuts import render
from . import forms
from .models import tire1_class, tire2_class

import csv

# Create your views here.
def admin_template(request):
    tire1_class.objects.all().delete()
    if (request.method=="POST"):
        if "dbsort" in request.POST:
            with open("tire1.csv", "r", encoding="utf-8") as f:
                reader=csv.reader(f)
                rows=[]
                for i in reader:
                    rows.append(i)
                for row in rows:
                    tire1_class.objects.create(
                        name=row[0].replace("\u3000",' '),
                        teaher=row[1].replace("\u3000",' '),
                        term=row[2].replace("\u3000",' '),
                        grade=row[3].replace("\u3000",' '),
                        major=row[4].replace("\u3000",' ')
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
    contents={
        "tire1_model":tire1_class.objects.all(),
        "tire2_model":tire2_class.objects.all(),
        "list_true":True,
        "term_spring":True
    }
    if request.method=="POST":
        if "list" in request.POST:
            contents["list_true"]=True
        elif "timeline" in request.POST:
            contents["list_true"]=False
        elif "spring" in request.POST:
            contents["list_true"]=False
            contents["term_spring"]=True
        elif "summer" in request.POST:
            contents["list_true"]=False
            contents["term_spring"]=False
        
    return render(request, 'home.html', contents)

def day_list_template(request, term, day, time):
    t1_models=[]
    for model in tire1_class.objects.all():
        (t_term,t_day,t_time)=str(model.term).split(' ')
        if (term==1 and t_term=="前期") or (term==2 and t_term=="後期"):
            if (day==1 and t_day=="月曜日") or (day==2 and t_day=="火曜日") or (day==3 and t_day=="水曜日") or (day==4 and t_day=="木曜日") or (day==5 and t_day=="金曜日"):
                if (time==1 and t_time=="１時限") or (time==2 and t_time=="２時限") or (time==3 and t_time=="３時限") or (time==4 and t_time=="４時限") or (time==5 and t_time=="５時限"):
                    t1_models.append(model)
    t2_models=[]
    for model in tire2_class.objects.all():
        (t_term,t_day,t_time)=str(model.term).split(' ')
        if (term==1 and t_term=="前期") or (term==2 and t_term=="後期"):
            if (day==1 and t_day=="月曜日") or (day==2 and t_day=="火曜日") or (day==3 and t_day=="水曜日") or (day==4 and t_day=="木曜日") or (day==5 and t_day=="金曜日"):
                if (time==1 and t_time=="１時限") or (time==2 and t_time=="２時限") or (time==3 and t_time=="３時限") or (time==4 and t_time=="４時限") or (time==5 and t_time=="５時限"):
                    t2_models.append(model)
    return render(request, 'day_list_template.html', {"t1_models":t1_models,"t2_models":t2_models})

def more_template(request, tire, class_id):
    if tire==1:
        class_data=tire1_class.objects.get(pk=class_id)
        eval="☆☆☆"
        detail="前年にこの教授のこの授業を受けた生徒が評価をしています。"
    elif tire==2:
        class_data=tire2_class.objects.get(pk=class_id)
        eval="☆☆"
        detail="前年にこの教授の授業を受けた生徒もしくは、この授業を受けた生徒が評価をしています。そのためこの評価は確実なものではありません。"
    contents={
        "class_data":class_data,
        "eval":eval,
        "detail":detail
    }
    return render(request, 'more.html', contents)