from django.urls import path


from .views import (
    RentaAutosClientsListSectionView,
    RentaAutosModulesSectionView,
)


app_name = 'renta_autos'
urlpatterns = [
    path('', RentaAutosModulesSectionView.as_view(), name="renta_autos_module"),
    path('cliente-lista/', RentaAutosClientsListSectionView.as_view(), name="renta_autos_clients_list"),
]
