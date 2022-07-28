from .models import (
    Renta
)

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


# Control the flow of save 
# transaction in DB.
def on_transaction_commit(func):
   def inner(*args, **kwargs):
      transaction.on_commit(lambda: func(*args, **kwargs))

   return inner



@on_transaction_commit
@receiver(post_save, sender=Renta)
def save_compra_realizada_to_cliente(sender, instance, created, **kwargs):

   cliente = instance.cliente
   cliente.compras_realizadas = cliente.rentas.count()
   cliente.save()