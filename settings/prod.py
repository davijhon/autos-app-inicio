from .base import *
import dj_database_url
import boto3


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# POSTGRES
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#    os.path.join(BASE_DIR, 'apps/clients/static'),
# )

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# WHITENOISE
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




#============= STATIC & MEDIA BACKEND AWS S3================#
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')



# Initializate s3 Bucker
s3 = boto3.resource(
   's3',
   aws_access_key_id=AWS_ACCESS_KEY_ID,
   aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)


AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = 'apps.clients.storages.ClientAvatarDNIStorage'

AWS_LOCATION = 'static'
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
   os.path.join(BASE_DIR, 'apps/clients/static'),
)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)



#============= lOGGING SYSTEM ================#
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, 
    'formatters':{
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'Simple_Format':{
            'format': '{levelname} {message}',
            'style': '{',
        }
    },
 
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            # 'class': 'logging.FileHandler',
            # 'filename': './logs/log_file1.log',
            'formatter':'Simple_Format',
        },
 
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
 
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },

}