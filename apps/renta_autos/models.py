from pyexpat import model
from django.db import models
from mirage import fields



def upload_to(instance, filename):
    return 'renta_autos/clients/{user_name}/{filename}'.format(
        user_name=instance.user_name, 
        filename=filename
    )

class Cliente(models.Model):
    fec_alta = models.DateTimeField(auto_now_add=True)
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
    avatar = models.ImageField(upload_to=upload_to, blank=True, null=True)
    fec_birthday = models.DateField()
    

    def __str__(self):
        return f"{self.cuenta_numero} - {self.user_name}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['fec_alta']
 
    def cantidad_compras_realizadas(self):
        pass


class AutoModelo(models.Model):
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo


class AutoTipo(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo


class AutoColor(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color


class Auto(models.Model):
    auto_name = models.CharField(max_length=100)
    modelo = models.ForeignKey(AutoModelo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(AutoTipo, on_delete=models.CASCADE)
    color = models.ForeignKey(AutoColor, on_delete=models.CASCADE)


    def __str__(self):
        return self.auto_name


class Renta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='rentas')


    def __str__(self):
        return "Renta: {auto} - por: {cli}".format(
            auto=self.auto,
            cli=self.cliente
        )