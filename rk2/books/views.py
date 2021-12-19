from django.db.models.aggregates import Avg
from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Library, Book
from django.db import models


def index(request):
    return render(request, 'index.html')

# BOOKS


def read_book(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})


def create_book(request):
    if request.method == 'GET':
        libraries = Library.objects.all()
        return render(request, 'book/create_book.html', {"libraries": libraries})
    else:
        dto = {}
        for key in request.POST:
            if key in Book.__dict__:
                dto[key] = request.POST[key]
        dto['library'] = get_object_or_404(Library, pk=request.POST['library'])
        new_book = Book(**dto)
        new_book.save()
        return redirect('read_book')


def update_book(request, book_id):
    if request.method == 'GET':
        libraries = Library.objects.all()
        book = get_object_or_404(Book, pk=book_id)
        return render(request, 'book/update_book.html', {"book": book, "libraries": libraries})
    else:
        book = get_object_or_404(Book, pk=book_id)
        for key in request.POST:
            if key in book.__dict__ and key != 'library':
                setattr(book, key, request.POST[key])
        if 'library' in request.POST:
            setattr(book, 'library', get_object_or_404(
                Library, pk=request.POST['library']))
        book.save()
        return redirect('read_book')


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect(request.META.get('HTTP_REFERER'))

# libraries


def read_library(request):
    libraries = Library.objects.all()
    return render(request, 'library/library_list.html', {'libraries': libraries})


def create_library(request):
    if request.method == 'GET':
        return render(request, 'library/create_library.html')
    else:
        new_library = Library(name=request.POST['name'])
        new_library.save()
        return redirect('read_library')


def update_library(request, library_id):
    if request.method == 'GET':
        library = get_object_or_404(Library, pk=library_id)
        return render(request, 'library/update_library.html', {"library": library})
    else:
        library = get_object_or_404(Library, pk=library_id)
        for key in request.POST:
            if key in library.__dict__:
                setattr(library, key, request.POST[key])
        library.save()
        return redirect('read_library')


def delete_library(request, library_id):
    library = get_object_or_404(Library, pk=library_id)
    library.delete()
    return redirect(request.META.get('HTTP_REFERER'))


# REPORT


def report(request):
    expensive_books = Book.objects.filter(cost__gt=1000)
    avg_prices = []
    for library in Library.objects.all():
        avg_prices.append({"library": library,  "price": Book.objects.filter(
            library=library.pk).aggregate(Avg('cost'))['cost__avg']})
    return render(request, 'report.html', {"expensive_books": expensive_books, "avg_prices": avg_prices})
