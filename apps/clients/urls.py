from django.urls import path


from .views import (
    ClientsListSectionView
)


app_name = 'clients'
urlpatterns = [
    path('', ClientsListSectionView.as_view(), name="clients_list_section"),
]
