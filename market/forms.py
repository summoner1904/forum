from django import forms


class MarketFilterForm(forms.Form):
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
        min_value=0, widget=forms.TextInput(attrs={
            'style': 'background: rgb(45,45,45);border-style:none;height: 35px; padding-left: 20px; color: rgb(255,255,255);',
            'placeholder': 'от'}), required=False
    )
    max_price = forms.IntegerField(
        min_value=1, widget=forms.TextInput(attrs={
            'style': 'background: rgb(45,45,45);border-style:none;height: 35px; padding-left: 20px; color: rgb(255,255,255);margin-top: 10px;',
            'placeholder': 'до'}), required=False
    )


class SellAccountForm(forms.Form):
    STYLE = {'style': 'background: #1f1f1f;border:none;height:40px;color:white;'
                      'padding-left:10px;display:block;margin-bottom: 20px;width: 90%;'
                      'margin: 0px auto;'}
    CHOICES_MAIL_PHONE = [
        ('Да', 'Да'),
        ('Нет', 'Нет')]
    CHOICES_COUNTRY = [
        ('Россия', 'Россия'),
        ('США', 'США'),
        ('Германия', 'Германия'),
        ('Нидерланды', 'Нидерланды'),
        ('Канада', 'Канада'),
        ('Китай', 'Китай'),
        ('Япония', 'Япония'),
        ('Франция', 'Франция'),
        ('Англия', 'Англия'),
    ]

    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs=STYLE), label='Название')
    nickname = forms.CharField(max_length=64, widget=forms.TextInput(attrs=STYLE), label='Никнейм')
    price = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs=STYLE), label='Цена (в рублях)')
    description = forms.CharField(max_length=12800, widget=forms.TextInput(attrs=STYLE), label='Описание')
    link = forms.CharField(max_length=64, widget=forms.TextInput(attrs=STYLE), label='Ссылка на аккаунт')
    phone = forms.ChoiceField(choices=CHOICES_MAIL_PHONE, widget=forms.Select(attrs=STYLE), label='Привязка к телефону')
    mail = forms.ChoiceField(choices=CHOICES_MAIL_PHONE, widget=forms.Select(attrs=STYLE), label='Привязка к почте')
    skins = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs=STYLE), label='Скины')
    country = forms.ChoiceField(choices=CHOICES_COUNTRY, widget=forms.Select(attrs=STYLE), label='Страна аккаунта')

