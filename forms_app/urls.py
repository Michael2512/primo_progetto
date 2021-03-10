from django.urls import pathfrom .views import contatti

app_name = 'forms_app'

urlpatterns = [
    path('contattaci/', contatti, name ='contatti'),
]