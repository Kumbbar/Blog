from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Your event', 'text': 'About what'}
        widgets = {
            'title': forms.Textarea(attrs={'cols': 40, 'rows': 0}),
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 30})
        }

