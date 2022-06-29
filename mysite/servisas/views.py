from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from django.views import generic
from django.core.paginator import Paginator

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
    paginator = Paginator(Automobilis.objects.all(),1)
    page_number = request.GET.get('page')
    paged_automobiliai = paginator.get_page(page_number)
    my_context = {'automobiliai': paged_automobiliai}
    return render(request, 'servisas/automobiliai.html', context=my_context)

def automobilis(request, automobilio_id):
    single_automobilis = get_object_or_404(Automobilis, pk=automobilio_id)
    return render(request, 'servisas/automobilis.html', context = {'automobilis': single_automobilis})


class UzsakymaiListVieW(generic.ListView):
    model = Uzsakymas
    paginate_by = 1
    
class UzsakymaiDetailView(generic.DetailView):
    model = Uzsakymas
    
    