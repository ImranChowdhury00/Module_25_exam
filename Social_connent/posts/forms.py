from django import forms
from .models import Post

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"] 
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',        
                'rows': 3,                  
                'placeholder': "What's on your mind"
            })
        }