from django import forms


class SettingsProfileForm(forms.Form):
    GENDER_CHOICES = [
        ("Mужской", "Мужской"),
        ("Женский", "Женский"),
        ("Неизвестно", "Неизвестно"),
    ]
    INPUT_STYLE = {
        "class": "d-inline-block",
        "style": "width: 60%;margin-left: 20px;border-style: none;"
                 "border-radius: 5px;color: rgb(255,255,255);"
                 "background: rgb(92,92,92);height: 35px;padding-left: 15px;",
    }
    username = forms.CharField(
        max_length=128,
        label="Никнейм",
        widget=forms.TextInput(attrs=INPUT_STYLE),
        required=False,
    )
    status = forms.CharField(
        max_length=128,
        label="Статус",
        widget=forms.TextInput(attrs=INPUT_STYLE),
        required=False,
    )
    avatar = forms.ImageField(
        widget=forms.FileInput(), label="Аватарка", required=False
    )
    telegram = forms.CharField(
        max_length=128,
        label="Telegram",
        widget=forms.TextInput(attrs=INPUT_STYLE),
        required=False,
    )
    discord = forms.CharField(
        max_length=128,
        label="Discord",
        widget=forms.TextInput(attrs=INPUT_STYLE),
        required=False,
    )
    date_birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "style": "padding-left:10px;border-style: none;"
                         "border-radius: 5px;color: rgb(255,255,255);"
                         "background: rgb(92,92,92);height: 35px;",
                "type": "date",
            }
        ),
        label="День рождения",
        required=False,
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={"style": "margin-bottom: 20px;"}),
        choices=GENDER_CHOICES,
        label="Пол",
        required=False,
    )


class PostProfileForm(forms.Form):
    text_post = forms.CharField(
        max_length=6144,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Напишите что-нибудь...",
                "style": "width: 75%;padding-left: 10px;border-style: none;"
                         "background: rgb(59,59,59);color: rgb(255,255,255);"
                         "margin-left: 10px;height: 40px;",
            }
        ),
    )
