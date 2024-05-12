from django import forms
from .models import Comment

class EmailPostForm(forms.Form): # inherits from Form class
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'name@example.com'}))
    to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1', 'placeholder': 'name@example.com'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1', 'rows': '3'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Comment'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField()