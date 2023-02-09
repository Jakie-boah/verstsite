from django.shortcuts import redirect, render


def my_orders(request):
    return render(request, './cabinet/myorders.html')


def my_tickets(request):
    return render(request, './cabinet/mytickets.html')


def my_paid_transactions(request):
    return render(request, './cabinet/myPaidTransactions.html')


def my_exchanger_tickets(request):
    return render(request, './myExchangerTickets.html')


def create_issue(request):
    return render(request, './cabinet/createIssue.html')


