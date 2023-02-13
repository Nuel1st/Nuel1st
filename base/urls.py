from django.urls import path
from . import views

urlpatterns = [
    path('insert_data/', views.insert_data, name='insert_data'),
    # path('profiles/', views.profiles, name='profiles' ),
]
