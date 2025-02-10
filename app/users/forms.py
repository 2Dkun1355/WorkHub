from datetime import date
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import JobSeekerProfile, Skill

UserModel = get_user_model()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ["username", "user_type", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if user.user_type == 'job_seeker':
                JobSeekerProfile.objects.get_or_create(user=user)
            # elif user.user_type == 'job_provider':
            #     JobProviderProfile.objects.get_or_create(user=user)
        return user

class UserForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')}, format='%Y-%m-%d'))

    class Meta:
        model = UserModel
        fields = ('photo', 'first_name', 'last_name', 'email', 'phone_number', 'telegram', 'birth_date')
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control', 'id': 'photo'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'photo': 'Photo',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'phone_number': 'Phone',
            'telegram': 'Telegram',
            'birth_date': 'Date of birth',
        }

class JobSeekerForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        label="Skills",
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-live-search': "true"}),
        required=False

    )

    class Meta:
        model = JobSeekerProfile
        fields = ["profile_title", "profile_info", "location", "skills", "english_level", "year_experience", "salary_expectations", "hourly_rate"]
        labels = {
            'profile_title': 'Profile title',
            'profile_info': 'About me',
            'location': 'Location',
            'english_level': 'English level',
            'year_experience': 'Year experience',
            'salary_expectations': 'Salary expectations (USD)',
            'hourly_rate': 'Hourly rate (USD)',
        }
        widgets = {
            'profile_title': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_info': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'english_level': forms.Select(attrs={'class': 'form-control'}),
            'year_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_expectations': forms.NumberInput(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }
