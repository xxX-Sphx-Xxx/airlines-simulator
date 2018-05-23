from django.urls import path
from . import views

urlpattern = [
path('accueil',views.home),
path('quelles-destinations',views.quelles_destinations),
path('quels-avions',views.quels_avions),
path('compare-hubs',views.compare_hubs),
path('compare_avions',views.compare_avions),
]