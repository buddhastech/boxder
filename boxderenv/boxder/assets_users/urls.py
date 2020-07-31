from django.urls import path
from .views import registration_form

urlpatterns = [
    path('registration/', registration_form, name="register")
]