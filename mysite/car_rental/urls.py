from django.urls import path
from .import views

app_name = "car_rental"

urlpatterns = [
    path('rental_review/', views.rental_review, name='rental_review'),
    path('thankyou/', views.thankyou, name='thankyou')
]
