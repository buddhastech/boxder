from django.urls import path
from .views import registration_form, user_register, user_login, boxder_index, boxder_admin
from .views import configuration, configuration_update, export_excel
from .views import asset_registration

urlpatterns = [
    path('registration/', registration_form, name="register"),
    path('regist/', user_register, name="regist"),
    path('login/', user_login, name="login"),
    path('boxder/', boxder_index, name="boxder"),
    path('administrator/', boxder_admin, name="adminBox"),
    path('registerAsset/', asset_registration, name="registerasset"),
    path('configuration/', configuration, name="configurationuser"),
    path('update_config/', configuration_update, name="configupdate"),
    path('export/', export_excel, name="exporexcel"),
]