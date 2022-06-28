from django.db import models

# Create your models here.

class Automobilio_modelis(models.Model):
    marke = models.CharField("Marke", max_length=50)
    modelis = models.CharField("Modelis",max_length=100)   
    
    def __str__(self):
        return f"{self.marke} {self.modelis}"
    
    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobiliu modeliai"
 
 
class Automobilis(models.Model):
    valstybinis_nr = models.CharField("Valstybinis nr", max_length=10, help_text="Valstybinis")
    automobilio_modelis_id = models.ForeignKey(Automobilio_modelis, on_delete=models.SET_NULL, null=True)     
    vin_kodas = models.CharField("VIN kodas", max_length=17)
    klientas = models.CharField("Klientas",max_length = 100)
    
    def __str__(self):
        return f"{self.automobilio_modelis_id}"
    
    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"   
  
   
class Uzsakymas(models.Model):
    
    data = models.DateField("Data", null=True)
    automobilis_id = models.ForeignKey(Automobilis, on_delete=models.SET_NULL,null =True)
    suma = models.FloatField("Suma")
    

    ORDER_STATUS = [
        ('a', 'Priimta'),
        ('i', 'Vykdoma'),
        ('d', 'Pabaigta'),
        ('c', 'Atmesta')
    ]

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='a',
        help_text='Statusas'
    )
    
    def __str__(self):
        return f"Automobilio {self.automobilis_id} serviso uzsakymas nr {self.id}, "
    
    class Meta:
        verbose_name = "Uzsakymas"
        verbose_name_plural = "Uzsakymai"
        
    def display_uzsakymo_eilutes_kaina(self):
        return list(automobilio.kaina for automobilio in self.uzsakymas.all())           
    
    
    display_uzsakymo_eilutes_kaina.short_description = 'Kaina'
    
    
class Paslauga(models.Model):
    pavadinimas = models.CharField("Paslaugos pavadinimas", max_length= 50)
    kaina = models.IntegerField()
        
    def __str__(self):
        return f"{self.pavadinimas}"             

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"
    
    def __str__(self):
        return f"{self.pavadinimas}"
    
class Uzsakymo_eilute(models.Model):
    
    paslaugos_id = models.ForeignKey(Paslauga, on_delete=models.SET_NULL, null=True)
    uzsakymo_id = models.ForeignKey(Uzsakymas, on_delete=models.CASCADE, null=True, related_name="uzsakymas")
    kaina = models.FloatField()
    
    def __str__(self):
        return f"{self.paslaugos_id} {self.uzsakymo_id}"    
    
    class Meta:
        verbose_name = "Uzsakymo eilute"
        verbose_name_plural = "Uzsakymu eilutes"      