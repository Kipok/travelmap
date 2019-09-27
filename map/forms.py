from django import forms
from .models import TravelRecord


class TravelRecordForm(forms.ModelForm):
    photos = forms.ImageField(required=False)

    class Meta:
        model = TravelRecord
        fields = ['place_name', 'desc', 'start_date', 'end_date', 'lon', 'lat']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place_name'].widget.attrs['class'] = 'form-control'
        self.fields['place_name'].widget.attrs['placeholder'] = 'Название места'
        self.fields['desc'].widget.attrs['class'] = 'form-control'
        self.fields['desc'].widget.attrs['placeholder'] = 'Что мы помним?'
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['placeholder'] = 'Дата начала'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['placeholder'] = 'Дата окончания'
        self.fields['lon'].widget.attrs['class'] = 'form-control small-form'
        self.fields['lon'].widget.attrs['placeholder'] = 'Долгота'
        self.fields['lat'].widget.attrs['class'] = 'form-control small-form'
        self.fields['lat'].widget.attrs['placeholder'] = 'Широта'

        self.fields['photos'].widget.attrs['class'] = 'custom-file-input'
        self.fields['photos'].widget.attrs['lang'] = 'ru'
        self.fields['photos'].widget.attrs['multiple'] = True


