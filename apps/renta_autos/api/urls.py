from django.urls import path


from .views import (
    ClienteListAPIView,
)


urlpatterns = [
    path('list', ClienteListAPIView.as_view(), name='clientes_list'),
]
