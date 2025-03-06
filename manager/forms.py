from django import forms

class major_select(forms.Form):
    data=[
        ("one", "文学部"),
        ("two", "法学部"),
        ("three", "経済学部"),
        ("four", "経営学部"),
        ("five", "理工学部")
    ]
    choices = forms.ChoiceField(label="学部を選択してください", choices=data)

class grade_select(forms.Form):
    data=[
        ("one","1年生"),
        ("two","2年生")
    ]