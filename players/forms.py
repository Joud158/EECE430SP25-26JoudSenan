from decimal import Decimal
from django import forms
from .models import VoleyPlayer


class VoleyPlayerForm(forms.ModelForm):
    class Meta:
        model = VoleyPlayer
        fields = ['name', 'date_joined', 'position', 'salary_payment', 'contact_person']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter player name'}),
            'date_joined': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Setter / Libero / Spiker...'}),
            'salary_payment': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coach / Manager / Parent'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Name must contain at least 2 characters.')
        return name

    def clean_position(self):
        position = self.cleaned_data.get('position', '').strip()
        if len(position) < 2:
            raise forms.ValidationError('Please enter a valid position.')
        return position

    def clean_contact_person(self):
        contact_person = self.cleaned_data.get('contact_person', '').strip()
        if len(contact_person) < 2:
            raise forms.ValidationError('Contact person name is too short.')
        return contact_person

    def clean_salary_payment(self):
        salary = self.cleaned_data.get('salary_payment')
        if salary is None:
            raise forms.ValidationError('Salary / payment is required.')
        if Decimal(salary) < 0:
            raise forms.ValidationError('Salary / payment cannot be negative.')
        return salary
