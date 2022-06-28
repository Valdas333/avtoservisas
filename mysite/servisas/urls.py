from django.urls import path
from . import views
from .views import serviso_redirektas, suma_sumarum, automobiliai

urlpatterns = [
    
    path('', serviso_redirektas),
    path('home/', views.home, name='home'),
    path('stats/', views.suma_sumarum, name='suma_sumarum'),
    path('automobiliai/', views.automobiliai, name ='automobiliai'),
    path('automobilis/<int:automobilio_id>', views.automobilis, name ='automobilis'),
    path('uzsakymai/', views.UzsakymaiListVieW.as_view(), name= 'uzsakymai'),
    path('uzsakymai/<int:pk>',views.UzsakymaiDetailView.as_view(), name ='uzsakymas'),
    
]