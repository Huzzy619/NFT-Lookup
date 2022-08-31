from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Settings(models.Model):
    logo = models.ImageField(upload_to = 'logo/')
    trade_mark = models.CharField(max_length = 225, default='Rarity Sniper')
    title = models.CharField(max_length=1000)
    slogan = models.TextField()


    class Meta:
        verbose_name = 'Setting'


class Statistics(models.Model):
    twitter = models.CharField(max_length=30, default="493k",
                               help_text="Simply update to current figure. add K for thousand or M for million at the end.")
    discord = models.CharField(max_length=30, default="321k",
                               help_text="Simply update to current figure. add K for thousand or M for million at the end.")

    class Meta:
        verbose_name = "Statistic"