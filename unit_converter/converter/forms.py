from django import forms

class TemperatureConversionForm(forms.Form):
    celsius = forms.FloatField(label='Celsius', required=True)