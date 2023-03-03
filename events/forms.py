from django import forms
from Users.models import Person
from .models import *
from datetime import date

CATEGORY_CHOICES=(
        ('Music','Music'),
        ('Sport','Sport'),
        ('Cinema','Cinema'),
)
class EventForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=150,
        widget= forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': "title",
            'placeholder': "Enter your title here"
        }
        )
    )
    description =forms.CharField(
        widget=forms.Textarea
    )
    imageEvent = forms.ImageField(label='Image')
    nbParticipants= forms.IntegerField(label="Number", min_value=0, step_size=1)
    category= forms.ChoiceField(
        widget=forms.RadioSelect, choices= CATEGORY_CHOICES
    )
    dateEvent= forms.DateField(
        widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form-control date-input' 
        }
        )
    )
    organized= forms.ModelChoiceField(
        queryset=Person.objects.all()
    )

class EventModelForm(forms.ModelForm):
    class Meta:
        model=Event
        field= "_all_"
        exclude= ['state']
        help_texts= {
            'title': 'Your event title here'
        }
    dateEvent= forms.DateField(
        initial=date.today(),
        widget= forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form-control date-input'
        }
    ))
