from datetime import date
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from common.models import Skill, JobFormat
from users.models import JobSeekerProfile, JobEmployerProfile

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
            elif user.user_type == 'job_employer':
                JobEmployerProfile.objects.get_or_create(user=user)
        return user

class UserForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ('photo', 'first_name', 'last_name', 'email', 'phone_number', 'telegram')
        labels = {
            'photo': 'Photo',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'phone_number': 'Phone',
            'telegram': 'Telegram',
        }
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control', 'id': 'photo'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
        }

class JobSeekerForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        label="Skills",
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-live-search': "true"}),
        required=False

    )
    job_format = forms.ModelMultipleChoiceField(
        queryset=JobFormat.objects.all(),
        label="Format",
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )

    class Meta:
        model = JobSeekerProfile
        fields = ["title", "description", "location", "skills", "job_format", "english_level", "year_experience", "salary_expectations"]
        labels = {
            'title': 'Profile title',
            'description': 'About me',
            'location': 'Location',
            'english_level': 'English level',
            'year_experience': 'Year experience',
            'salary_expectations': 'Salary expectations (USD)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'english_level': forms.Select(attrs={'class': 'form-control'}),
            'year_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_expectations': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class JobEmployerForm(forms.ModelForm):
    class Meta:
        model = JobEmployerProfile
        fields = ["logo", "company_name", "company_description","company_url", "location"]
        labels = {
            'logo': 'Logo',
            'company_name': 'Company name',
            'company_description': 'About company',
            'company_url': 'Company website',
            'location': 'Location',
        }
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'form-control', 'id': 'photo'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_description': forms.Textarea(attrs={'class': 'form-control'}),
            'company_url': forms.URLInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }