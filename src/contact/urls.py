from django.urls import path
from . import views
app_name = 'contact'

urlpatterns = [
    path('', views.contact, name="contact"),
    path('send_contact_email/', views.send_contact_email, name='send_contact_email'),
]
