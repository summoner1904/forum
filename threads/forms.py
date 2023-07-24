from django import forms
from .models import Category


class NewThreadForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'border: none; background: #2f2f2f;height: 40px; width: 60%;padding-left: 20px; color: white;'}))
    text = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'style': 'background: #2f2f2f;border:none;padding: 10px 0 0 20px;color: white;width: 60%;height: 300px;'}))
    screen = forms.ImageField(widget=forms.FileInput(attrs={'id': 'id_screen'}), required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, widget=forms.Select(attrs={'style': 'background: #2f2f2f;color: white;width: 60%;height:30px;'}), label='Категория')


class NewCommentForm(forms.Form):
    comment = forms.CharField(max_length=10000, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'placeholder': 'Сообщение...', 'class': 'reply-input-cls'}))