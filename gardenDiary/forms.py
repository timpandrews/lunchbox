from django import forms

from gardenDiary.models import post


class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = [
            "title",
            "content",
        ]