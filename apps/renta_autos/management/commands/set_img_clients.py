import os
import random
import ast

from django.db import transaction
from django.conf import settings
from django.core.management.base import BaseCommand
from datetime import datetime


from utils.get_file_obj import get_file_obj
from apps.clients.models import Cliente



BASE_DIR = settings.BASE_DIR



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for cli in Cliente.objects.all():
            c = random.choice([1, 2, 3, 4, 5])
            avatar_file_content = get_file_obj(f"static/src/img/avatar{c}.png", "PNG") 
            dni_photo_file_content = get_file_obj(f"static/src/img/480.jpg", "JPEG") 

            cli.avatar.save(f"avatar{c}.png", avatar_file_content) 
            cli.foto_dni.save("480.jpg", dni_photo_file_content) 

            cli.save()
        print("Done!")