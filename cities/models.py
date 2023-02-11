from django.db import models

# Create your models here.


class City(models.Model):
    city = models.CharField(verbose_name='Город', max_length=50, unique=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'