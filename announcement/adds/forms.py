from django import forms
from .models import Advertisement, Reply
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AddsForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Advertisement
        # fields = '__all__'
        fields = ['title', 'text', 'category']


class ReplyForm(forms.ModelForm):

    class Meta:
       model = Reply
       fields = ['text']

