from django import forms
from adminuser.models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
            'reply'
        ]