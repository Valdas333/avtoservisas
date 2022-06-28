from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from django.views import generic

# Create your views here.
def home(request):
    return render(request, 'servisas/base.html')

def about(request):
    return render(request, 'servisas/about.html')

def serviso_redirektas(request):
    return HttpResponseRedirect('about/')

def suma_sumarum(request):
    uzsakymu_kiekis = Uzsakymas.objects.all().count()
    paslaugu_kiekis = Paslauga.objects.all().count()
    automobiliu_kiekis = Automobilis.objects.all().count()
    
    context = {
        'uzsakymu_kiekis': uzsakymu_kiekis,
        'paslaugu_kiekis': paslaugu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis    
    }
    return render(request, 'servisas/stats.html', context=context)

def automobiliai(request):   
    automobiliai = Automobilis.objects.all()
    my_context = {'automobiliai': automobiliai}
    return render(request, 'servisas/automobiliai.html', context=my_context)

def automobilis(request, automobilio_id):
    single_automobilis = get_object_or_404(Automobilis, pk=automobilio_id)
    return render(request, 'servisas/automobilis.html', context = {'automobilis': single_automobilis})


class UzsakymaiListVieW(generic.ListView):
    model = Uzsakymas
    
    
class UzsakymaiDetailView(generic.DetailView):
    model = Uzsakymas
    
    