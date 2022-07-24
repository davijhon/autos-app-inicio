from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
	# Django APPS
	path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),

	# RESTful API FM ADMIN endpoints
    path('api/clientes/', include('apps.clients.api.urls')),

	# Local APPS
	path('', include('apps.clients.urls', namespace='clients'))


]



if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)