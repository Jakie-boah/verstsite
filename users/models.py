from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

# Create your models here.


class UserProfile(AbstractUser):
    username = None
    user_login = models.CharField(verbose_name='Логин', max_length=50, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=50)
    socials = models.CharField(verbose_name='Jabber/telegram', max_length=50)
    balance = models.FloatField(verbose_name='Баланс', default=0.0)

    USERNAME_FIELD = 'user_login'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Orders(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name='Пользователь')
    number = models.CharField(verbose_name='Номер', unique=True, max_length=25)
    item = models.CharField(verbose_name='Товар', max_length=25)
    city = models.CharField(verbose_name='Город', max_length=25)
    address = models.CharField(verbose_name='Адрес', max_length=50)
    price = models.IntegerField(verbose_name='Цена')
    paid = models.BooleanField(verbose_name='Оплачен', default=False)
    payment_method = models.CharField(verbose_name='Метод оплаты', max_length=25)
    date = models.DateTimeField(verbose_name='Дата покупки')
    found = models.BooleanField(verbose_name='Найден', default=False)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Tickets(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name='Пользователь')
    number = models.CharField(verbose_name='Номер', unique=True, max_length=25)
    date = models.DateTimeField(verbose_name='Дата')
    thema = models.CharField(verbose_name='Тема', max_length=50)
    answers = models.CharField(verbose_name='Ответов', max_length=50)
    type = models.CharField(verbose_name='Тип', max_length=50)
    status = models.BooleanField(verbose_name='Статус', default=False)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'


class MyPaidTransactions(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name='Пользователь')
    number = models.CharField(verbose_name='Номер', unique=True, max_length=25)
    date = models.DateTimeField(verbose_name='Дата')
    amount = models.IntegerField(verbose_name='Сумма')
    total_amount = models.IntegerField(verbose_name='К оплате')
    requisites = models.CharField(verbose_name='Реквизиты', max_length=100)
    method = models.CharField(verbose_name='Метод', max_length=50)
    type_process = models.CharField(verbose_name='Тип процедуры', max_length=50)
    in_place = models.BooleanField(verbose_name='Зачислен', default=False)
    status = models.BooleanField(verbose_name='Статус', default=False)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
