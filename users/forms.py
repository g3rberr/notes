from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


from .models import User



from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control no_borders dark-input',
            'autocomplete': 'username',
            'required': 'required'
        })
    )
    password = forms.CharField(
        label='Passworda',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control dark-input',
            'autocomplete': 'current-password',
            'required': 'required'
        })
    )


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control no_borders dark-input',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control no_borders dark-input',}))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control no_borders dark-input',}),
            'email': forms.TextInput(attrs={'class': 'form-control no_borders dark-input',}),
        }

class ChangeEmailForm(forms.ModelForm):
    current_password = forms.CharField(
        label="Current password",
        widget=forms.PasswordInput(attrs={'class': 'form-control no_borders dark-input'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('email', )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control no_borders dark-input'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


    def clean_current_password(self):
        password = self.cleaned_data.get('current_password')
        if not self.user.check_password(password):
            raise forms.ValidationError('Incorrect password')
        print('работает', password)
        return password
    


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control no_borders dark-input', 'placeholder': 'old password'})
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control no_borders dark-input', 'placeholder': 'new password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control no_borders dark-input', 'placeholder': 'confirm new password'})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        password = self.cleaned_data.get('old_password')
        if not self.user.check_password(password):
            raise forms.ValidationError('Incorrect current password')
        return password

    def clean_new_password(self):
        password = self.cleaned_data.get('new_password')
        try:
            validate_password(password, self.user)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    def clean(self):
        cleaned_data = super().clean()
        new = cleaned_data.get('new_password')
        confirm = cleaned_data.get('confirm_password')
        if new and confirm and new != confirm:
            raise forms.ValidationError('New passwords do not match')
        return cleaned_data

    def save(self, commit=True):
        new_password = self.cleaned_data['new_password']
        self.user.set_password(new_password)
        if commit:
            self.user.save()
        return self.user
