from django import forms

class major_grade_select(forms.Form):
    major_data=[
        ("one", "文学部"),
        ("two", "法学部"),
        ("three", "経済学部"),
        ("four", "経営学部"),
        ("five", "理工学部")
    ]
    grade_data=[
        ("one","1年生"),
        ("two","2年生"),
        ("three","3年生"),
        ("four","4年生"),
    ]

    major_choices = forms.ChoiceField(label="学部を選択してください", choices=major_data)
    grade_choices = forms.ChoiceField(label="学年を選択してください", choices=grade_data)