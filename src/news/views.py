from django.shortcuts import render

from news.models import Notification

# Create your views here.

def news(request):
    notifications = Notification.objects.all()
    context={
        'notifications': notifications,
    }
    return render(request, 'news/news.html', context=context)