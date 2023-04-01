from django import forms 
from .models import Comment ,Author ,Post


class TagForm(forms.Form):
    name=forms.CharField(max_length=25, min_length=6)
    

class AuthForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'article', 'author', ]
        widgets={
            'title' : forms.TextInput(attrs={'class': 'h-full-width' , 'placeholder':'Title'}),
            'author' : forms.TextInput(attrs={'class': 'h-full-width' , 'placeholder':'Author'}),
            'article' : forms.Textarea(attrs={'class': 'h-full-width' , 'placeholder':'Type your Articles here'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name', 'email', 'comment']
        widgets={
            'name' : forms.TextInput(attrs={' class ': 'h-full-width' , 'placeholder':'your name', 'id': 'cName'}),
            'email' : forms.TextInput(attrs={' class ': 'h-full-width' , 'placeholder':'your email', 'id': 'cEmail'}),
            'comment' : forms.Textarea(attrs={' class ': 'h-full-width' , 'placeholder':'your comment', 'id': 'cMessage'})
        }


        