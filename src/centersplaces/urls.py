from django.urls import path
from . import views
app_name = 'centersplaces'

urlpatterns = [
    path('', views.centersplaces, name="centersplaces"),
    path('<int:center_id>/dates', views.centerdates, name="centerdates"),
]


