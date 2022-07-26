import os
from rest_framework import serializers
from django.conf import settings

from apps.renta_autos.models import Cliente



class ListClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
            "fec_alta",
            "user_name",
            "codigo_zip",
            # "credit_card_num",
            # "credit_card_ccv",
            "cuenta_numero",
            # "direccion",
            # "geo_latitud",
            # "geo_longitud",
            "color_favorito",
            # "foto_dni",
            # "ip",
            # "avatar",
            "fec_birthday",
        )

    def to_representation(self, instance):
        rep = super(ListClientesSerializer, self).to_representation(instance)


        rep['cuenta_numero'] = '***************'
        # rep['direccion'] = '***************'
        # rep['geo_latitud'] = '***************'
        # rep['geo_longitud'] = '***************'
        # rep['ip'] = '***************'
        # rep['credit_card_num'] = '***************'
        # rep['credit_card_ccv'] = '***************'
        # rep['avatar'] = os.path.join(settings.STATIC_URL, 'src/img/user_no_profile.png')
        # rep['foto_dni'] = os.path.join(settings.STATIC_URL, 'src/img/dni_black.png')

        return rep