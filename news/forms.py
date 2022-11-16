from django import forms
from .models import Post


class NewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text', 'rating']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text', 'rating']
