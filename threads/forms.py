from django import forms


class NewThreadForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'border: none; background: #2f2f2f;height: 40px; width: 60%;padding-left: 20px; color: white;'}))
    text = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'style': 'background: #2f2f2f;border:none;padding: 10px 0 0 20px;color: white;width: 60%;height: 300px;'}))
    screen = forms.ImageField(widget=forms.FileInput(attrs={'id': 'id_screen'}), required=False)
