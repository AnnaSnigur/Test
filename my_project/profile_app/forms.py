from django import forms
from profile_app.models import Profile
from django.forms import DateInput


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('username', 'password', 'password2', 'birth_date')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords not equal!')
        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.save()
        return user


class EditForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=DateInput(attrs={
            'type': 'date',
            'class': 'datepicker'
        }
        ))

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'biography',
            'contacts',
        )
