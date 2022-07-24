import os
from io import BytesIO
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
import boto3
import botocore

from PIL import Image


BASE_DIR = settings.BASE_DIR



def get_file_obj(path, format, file_type='img'):
	buffer = BytesIO()


	if settings.DEBUG:
		file_path = os.path.join(BASE_DIR, path)
		if os.path.exists(file_path):
			if file_type == 'img':
				file_obj = Image.open(file_path)

	else:
		pass

	file_obj.save(buffer, format=format)
	buffer.seek(0)
	if file_type == 'img':
		content_file = ContentFile(buffer.read())


	return content_file