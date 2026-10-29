from django import forms
import re


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']

        pattern = r'[A-Za-z][A-Za-z0-9_]{2,29}'

        if not re.fullmatch(pattern, username):
            raise forms.ValidationError(
                "Username must start with a letter and contain 3-30 letters, numbers or underscores."
            )

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%!]).{8,}'

        if not re.fullmatch(pattern, password):
            raise forms.ValidationError(
                "Password must contain uppercase, lowercase, digit, special character and at least 8 characters."
            )

        return password
