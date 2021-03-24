from django.urls import path
from .views import homepage, menu, chi_siamo, variabili, index

app_name='prima_app'
urlpatterns = [
    path('welcome/', homepage, name='homepage'),
    path('menu/', menu, name='menu'),
    path('chi_siamo/', chi_siamo, name='chi-siamo'),
    path('variabili/', variabili, name = 'variabili'),
    path('index/', index, name = 'index')
]