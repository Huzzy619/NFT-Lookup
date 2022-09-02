from .settings import *
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nft-lookup.herokuapp.com','nft-lookout-production.up.railway.app']

DATABASES = {
    "default": dj_database_url.config()
}



