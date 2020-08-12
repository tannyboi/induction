from .models import edu_history
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = edu_history
        fields = ('subject', 'percentage', 'institution')