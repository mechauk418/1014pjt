from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title','content','movie_name','grade')
        labels = {
            'title': '제목',
            'content': "내용",
            'movie_name': '영화 제목',
        }