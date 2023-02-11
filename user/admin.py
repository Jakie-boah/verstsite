from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Orders)
admin.site.register(Tickets)
admin.site.register(MyPaidTransactions)
