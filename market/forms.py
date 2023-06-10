from django import forms


class MarketFilterForm(forms.Form):
    # Стили для Инпутов
    INPUT_STYLE = {
        "style": "margin-top: 15px;background: rgb(45,45,45);"
        "border-style: none;height: 30px;padding-left: 20px;color: rgb(255,255,255);",
        "class": "d-inline-block",
    }

    title_input = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "style": "margin-top:15px;background:rgb(45,45,45);border-style:none;"
                         "height:40px;padding-left:20px;color:rgb(255,255,255);width: 100%;",
                "class": "d-inline-block",
                "placeholder": "Поиск",
            }
        ),
        required=False,
    )
    min_price = forms.IntegerField(
        min_value=0, widget=forms.TextInput(attrs={'style': 'background: rgb(45,45,45);border-style:none;height: 35px; padding-left: 20px; color: rgb(255,255,255);', 'placeholder': 'от'}), required=False
    )
    max_price = forms.IntegerField(
        min_value=1, widget=forms.TextInput(attrs={'style': 'background: rgb(45,45,45);border-style:none;height: 35px; padding-left: 20px; color: rgb(255,255,255);', 'placeholder': 'до'}), required=False
    )
