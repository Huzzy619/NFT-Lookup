from .settings import *
import os
# import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nft-lookup.herokuapp.com','nft-lookout.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://nft-lookout.up.railway.app']


# DATABASES = {
#     "default": dj_database_url.config()
# }

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['CLOUD_API_KEY'],
    'API_SECRET': os.environ['CLOUD_API_SECRET'],
}

