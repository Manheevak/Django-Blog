from  django import forms
from .models import Blog

from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['date']
        