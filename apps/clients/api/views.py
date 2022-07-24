from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .pagination import CustomPagination


from apps.clients.models import Cliente

from .serializers import (
	ListClientesSerializer,
)




class ClienteListAPIView(ListAPIView):
	serializer_class = ListClientesSerializer
	pagination_class = CustomPagination
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		queryset = Cliente.objects.all()

	# 	query = self.request.GET.get('query')

	# 	if query is not None and query != '':
	# 		queryset = queryset.filter(
    #         	Q(nombre__icontains=query) |
    #         	Q(rif__icontains=query)).distinct()

		return queryset