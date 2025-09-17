from django import forms
from . models import post

class Post_Form(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ['title','content']
