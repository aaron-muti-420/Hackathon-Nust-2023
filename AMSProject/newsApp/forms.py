from django import forms
from .models import Comment

# CREATE THE CLASS TO SEND THE EMAILS USING NON MODEL TIED FORMS
class EmailShareForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

"""
1. GO AND ENABLE THIS FORM INSIDE THE VIEW
2. CREATE THE MODELFORMS TO ENABLE THE FEATURE OF THE MODELFORMS
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


