from django.contrib import admin
from .models import Automobilis, Uzsakymo_eilute, Automobilio_modelis, Paslauga, Uzsakymas
# Register your models here.


class UzsakymoEilutesInline(admin.TabularInline):
    model = Uzsakymo_eilute
    extra = 0 # išjungia placeholder'ius


class UzsakymasAdmin(admin.ModelAdmin):
    # fields = ('data','suma')
    # list_display = ['automobilis_id', 'data', 'suma']
    # list_display_links = ('data', 'suma')
    # list_editable = ('suma', 'display_uzsakymas')
    inlines = [UzsakymoEilutesInline]
    

# class AutomobilisAdminInline(admin.TabularInline):
#     model = Automobilis
    
class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ['automobilio_modelis_id','valstybinis_nr', 'vin_kodas', 'klientas']
    list_filter = ('klientas', 'automobilio_modelis_id')
    search_fields = ('vin_kodas', 'valstybinis_nr', 'automobilio_modelis_id__modelis')


class UzsakymoEiluteAdmin(admin.ModelAdmin):
    list_display = ['paslaugos_id', 'kaina']
    
    
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymo_eilute, UzsakymoEiluteAdmin)
admin.site.register(Automobilio_modelis)
admin.site.register(Paslauga)
admin.site.register(Uzsakymas, UzsakymasAdmin)