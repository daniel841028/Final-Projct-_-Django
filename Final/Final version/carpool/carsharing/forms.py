from django import forms
from .models import User

forms.DateTimeInput.input_type="datetime-local" 

class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=256,widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):

    name = forms.CharField(label="Username", max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", max_length=256,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(initial='@jhu.edu', label="email",
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@jhu.edu'):
            raise forms.ValidationError(
                "Only @jhu.edu email addresses allowed")
        return email


class DriverForm(forms.Form):

    time = forms.DateTimeField(label="Time ( Departure )", widget=forms.DateTimeInput(
        attrs={'class': 'form-control'}))
    departure = forms.CharField(label="Departure", max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    destination = forms.CharField(label="Destination", max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
