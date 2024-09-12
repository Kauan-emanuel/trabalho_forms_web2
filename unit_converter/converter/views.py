from django.shortcuts import render
from .forms import TemperatureConversionForm


def index(request):
    resultado = None
    if request.method == 'POST':
        form = TemperatureConversionForm(request.POST)
        if form.is_valid():
            celsius = form.cleaned_data['celsius']
            fahrenheit = (celsius * 9/5) + 32
            resultado = f'{celsius}°C é igual a {fahrenheit}°F'
    else:
        form = TemperatureConversionForm()

    return render(request, 'converter/index.html', {'form': form, 'resultado': resultado})