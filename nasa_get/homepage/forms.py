from django import forms


class UserAPIForm(forms.Form):
    api_key = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "placeholder": "API Key",
                "name": "api_input",
                "id": "api_input",
            }
        )
    )
