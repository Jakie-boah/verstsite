from .cabinet import *
from .authentication.login import *
from .authentication.logout import *
from .authentication.register import *
# Create your views here.


def cabinet(request):
    return render(request, './cabinet/cabinet.html')


def balance(request):
    return render(request, './cabinet/balance/balance.html')