from django.shortcuts import render
from accounts.models import Account
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# Create your views here.

def contact(request):
    account_data = Account.objects.first()
    context={
        "account":account_data
    }
    return render(request, 'contact/contact.html',context=context)



@csrf_exempt
def send_contact_email(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        sender_mail = request.POST.get('sender_mail')
        sent_message = request.POST.get('sent_message')
        receiver_mail = request.POST.get('receiver_mail')

        subject = f"New message from {sender_name}"
        message = f"Sender Name: {sender_name}\nSender Email: {sender_mail}\n\nMessage:\n{sent_message}"

        send_mail(subject, message, sender_mail, [receiver_mail], fail_silently=False)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'fail'}, status=400)
