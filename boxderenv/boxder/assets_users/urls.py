from django.urls import path
from .views import registration_form, user_register

urlpatterns = [
    path('registration/', registration_form, name="register"),
    path('regist/', user_register, name="regist")
]