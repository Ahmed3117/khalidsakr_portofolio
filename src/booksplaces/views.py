from django.shortcuts import render

from booksplaces.models import Book, Library
from centersplaces.models import Class, Government

# Create your views here.

def booksplaces(request):
    governments = Government.objects.all()
    libraries = Library.objects.all()
    context={
        'governments': governments,
        'libraries': libraries,
    }
    return render(request, 'booksplaces/libraries.html',context=context)


def books(request,library_id):
    library = Library.objects.get(id=library_id)
    books = Book.objects.filter(library=library)
    classes = Class.objects.all()
    context={
        'library': library,
        'books': books,
        'classes': classes,
    }
    return render(request, 'booksplaces/librarybooks.html',context=context)