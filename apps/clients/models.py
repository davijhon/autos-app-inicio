from django.db import models
from mirage import fields


def upload_to(instance, filename):
    return 'clients/{user_name}/{filename}'.format(
        user_name=instance.user_name, 
        filename=filename
    )

class Cliente(models.Model):
    fec_alta = models.DateTimeField()
    user_name = models.CharField(max_length=150)
    codigo_zip = models.CharField(max_length=50)
    credit_card_num = fields.EncryptedCharField()
    credit_card_ccv = fields.EncryptedCharField()
    cuenta_numero = models.IntegerField()
    direccion = models.CharField(max_length=250)
    geo_latitud = models.FloatField()
    geo_longitud = models.FloatField()
    color_favorito = models.CharField(max_length=100)
    foto_dni = models.ImageField(upload_to=upload_to, blank=True, null=True)
    ip = models.CharField(max_length=15)
    auto = models.CharField(max_length=250)
    auto_modelo = models.CharField(max_length=250)
    auto_tipo = models.CharField(max_length=250)
    auto_color = models.CharField(max_length=250)
    cantidad_compras_realizadas = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to=upload_to, blank=True, null=True)
    fec_birthday = models.DateTimeField()
    

    def __str__(self):
        return f"{self.cuenta_numero} - {self.user_name}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['fec_alta']