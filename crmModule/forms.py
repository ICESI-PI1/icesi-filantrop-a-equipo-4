from django.forms import ModelForm
from .models import Sponsor
from .models import Event
from django import forms
from .models import Sponsor_Event
from .models import Sponsor, Event
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SponsorForm(ModelForm):
    class Meta:
        model= Sponsor
        fields = ['name', 'personType','contact_number','email','previousColab']
        labels = {
            'name': 'Nombre',
            'personType': 'Tipo de persona',
            'contact_number': 'Número de contacto',
            'email': 'Correo electrónico',
            'previousColab': '¿La persona ha colaborado antes con icesi?',
        }
        OPCIONES = [('si', 'Sí'), ('no', 'No')]

        previousColab = forms.ChoiceField(
        choices=OPCIONES,
        widget=forms.RadioSelect(),
        label='¿La persona ha colaborado antes con Icesi?')
        
class EventForm(ModelForm):
    class Meta:
        model= Event
        fields = ['name','date','event_Type','time']
        
        labels={
            'name':'Nombre', 'date':'Fecha','time':'Hora', 'event_Type':'Tipo de Evento'
            }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'})
        }

class EventSearchForm(forms.Form):
    nombre_evento = forms.CharField(required=False, label='Buscar por nombre')
    fecha_evento = forms.DateField(required=False, label='Buscar por fecha', widget=forms.DateInput(attrs={'type': 'date'}))

class SponsorEventForm(forms.ModelForm):
    class Meta:
        model = Sponsor_Event
        fields = ['Sponsor_id', 'participation']

class CombinedForm(forms.ModelForm):
    name = forms.CharField(label='Nombre del Evento')
    date = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    event_Type = forms.ChoiceField(choices=Event.type, label='Tipo de Evento')
    
    sponsor_name = forms.ModelChoiceField(queryset=Sponsor.objects.all(), label='Patrocinador', to_field_name='name')

    class Meta:
        model = Sponsor_Event
        fields = ['sponsor_name', 'participation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sponsor_name'].required = True
        self.fields['participation'].required = True

    def clean_sponsor_name(self):
        sponsor_name = self.cleaned_data['sponsor_name']
        sponsor = Sponsor.objects.get(name=sponsor_name)
        return sponsor.id  # Devolvemos el ID del patrocinador

User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email','username']

