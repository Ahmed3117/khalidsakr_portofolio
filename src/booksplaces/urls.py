from django.urls import path
from . import views
app_name = 'booksplaces'

urlpatterns = [
    path('', views.booksplaces, name="booksplaces"),
    path('<int:library_id>/books', views.books, name="books"),
]

