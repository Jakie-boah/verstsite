from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .handlers.ac_manager import AccountManager


class UserProfile(AbstractBaseUser):
    user_login = models.CharField(verbose_name='Логин', max_length=50, unique=True)
    socials = models.CharField(verbose_name='Jabber/telegram', max_length=50, null=True, blank=True)
    password = models.CharField(verbose_name='Пароль', max_length=150)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_login'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.user_login

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

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
