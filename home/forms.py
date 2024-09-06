from django import forms
from django.core.exceptions import ValidationError
from .models import ListModel

class ListForm(forms.ModelForm):
    class Meta:
        model = ListModel
        fields = ['show', 'title', 'description', 'date', 'time']
        widgets = {
            'show': forms.CheckboxInput(attrs={
                'class': 'complete-task',
            }),

            'title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Titulo'
            }),

            'description': forms.TextInput(attrs={
                'class': 'input description',
                'placeholder': 'Descrição'
            }),

            'date': forms.DateInput(attrs={
                'class': 'input',
                'placeholder': 'dd/mm/aaaa'
            }),

            'time': forms.TimeInput(attrs={
                'class': 'input',
                'placeholder': 'h:m:s'})
        }  

    def clean_date(self):
        date = self.cleaned_data.get('date')

        if not date:
            if date is None:
                return date
            else:
                raise ValidationError('', code='invalid')
        
        return date
    
    def clean_time(self):
        time = self.cleaned_data.get('time')

        if not time:
            if time is None:
                return time
            else:
                raise ValidationError('', code='invalid')
        
        return time





            

