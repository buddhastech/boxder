from django.urls import path
from .views import registration_form, user_register, user_login

urlpatterns = [
    path('registration/', registration_form, name="register"),
    path('regist/', user_register, name="regist"),
    path('login/', user_login, name="login")
]