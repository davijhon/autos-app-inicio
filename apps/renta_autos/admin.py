from django.contrib import admin

from .models import ( Cliente, Auto, Renta, 
AutoModelo, AutoTipo, AutoColor )



@admin.register(Cliente)
class RentaAutosClienteAdmin(admin.ModelAdmin):
	list_display = [
		'cuenta_numero', 
		'user_name', 
		'fec_alta', 
	]
	search_fields = ['cuenta_numero']

admin.site.register(Auto)
admin.site.register(Renta)
admin.site.register(AutoModelo)
admin.site.register(AutoTipo)
admin.site.register(AutoColor)

