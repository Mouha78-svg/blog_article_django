from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model: Comment
        exclude = ["post"]
        labels = {
            "user_name" : "Votre nom",
            "user_email" : "votre email",
            "text" : "commenter"
        }

        