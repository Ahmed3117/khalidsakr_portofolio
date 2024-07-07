from django.shortcuts import render

from accounts.models import Account

# Create your views here.

def index(request):
    account_data = Account.objects.first()
    context={
        "account":account_data
    }
    return render(request, 'accounts/index.html',context=context)
