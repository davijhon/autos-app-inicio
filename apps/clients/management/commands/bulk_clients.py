from lib2to3.pytree import Base
import os
import random
import ast

from django.db import transaction
from django.conf import settings
from django.core.management.base import BaseCommand
from datetime import datetime


# from utils.get_file_obj import get_file_obj
from apps.clients.models import Cliente


BASE_DIR = settings.BASE_DIR

sample_db_path = os.path.join(BASE_DIR, 'sample_db/db.txt')


def convert_str_datetime_to_datetime_obj(fec_alta):
    fec_alta_splited = fec_alta.split('T')
    time_splited = fec_alta_splited[1].split('Z')

    d = fec_alta_splited[0]
    t = time_splited[0]
    dt = f"{d} {t}"

    return datetime.fromisoformat(dt)




class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open(sample_db_path, 'r') as f:
            clients_records = ast.literal_eval(f.read())

        for cr in clients_records:
            user_name = cr['user_name']

            cli = Cliente.objects.get(user_name=user_name)
            cli.credit_card_num = cr['credit_card_num']
            cli.save()

            # with transaction.atomic():
            #     client = Cliente(
            #         fec_alta=convert_str_datetime_to_datetime_obj(cr['fec_alta']),
            #         user_name=cr['user_name'],
            #         codigo_zip=cr['codigo_zip'],
            #         credit_card_num=cr['codigo_zip'],
            #         credit_card_ccv=cr['credit_card_ccv'],
            #         cuenta_numero=cr['cuenta_numero'],
            #         direccion=cr['direccion'],
            #         geo_latitud=cr['geo_latitud'],
            #         geo_longitud=cr['geo_longitud'],
            #         color_favorito=cr['color_favorito'],
            #         ip=cr['ip'],
            #         auto=cr['auto'],
            #         auto_modelo=cr['auto_modelo'],
            #         auto_tipo=cr['auto_tipo'],
            #         auto_color=cr['auto_color'],
            #         cantidad_compras_realizadas=cr['cantidad_compras_realizadas'],
            #         fec_birthday=convert_str_datetime_to_datetime_obj(cr['fec_birthday']),
            #     )
                
            #     client.save()



        print("Done!")