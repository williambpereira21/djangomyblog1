# djangomyblog/blog/forms_comment.py
from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  # Apenas o campo 'comment' será exibido
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Digite seu comentário aqui...',
                    'class': 'comment-textarea'
                }
            ),
        }
        labels = {
            'comment': ''  # Remove o label do campo, opcional
        }
