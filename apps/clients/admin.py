from django.contrib import admin

from .models import Cliente



@admin.register(Cliente)
class ClientAdmin(admin.ModelAdmin):
	list_display = [
			'cuenta_numero', 
			'user_name', 
			'cantidad_compras_realizadas',
			'fec_alta', 
			'codigo_zip', 
	]
	list_filter = [
        'cuenta_numero', 
        'cantidad_compras_realizadas', 
        'fec_alta'
    ]