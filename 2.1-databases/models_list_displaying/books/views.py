from django.shortcuts import render,redirect
from books.models import Book
from itertools import groupby
from operator import itemgetter


def index(request):
    return redirect('books')


def books_view(request, date=None):
    template = 'books/books_list.html'
    books = Book.objects.order_by("pub_date")
    prev_date, next_date = '', ''
    if date:
        filtered_books = books.filter(pub_date=date)
        first = filtered_books.first()
        last = filtered_books.last()
        prev_book = books.filter(pub_date__lt=first.pub_date).last()
        if prev_book:
            prev_date = prev_book.pub_date
         
        next_book = books.filter(pub_date__gt=last.pub_date).first()
        if next_book:
            next_date = next_book.pub_date
        books = filtered_books
    context = {
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date
        }
    return render(request, template, context)
