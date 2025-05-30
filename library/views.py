from django.shortcuts import render
from django.http import HttpResponse
from .forms import AuthorForm, BookForm
from .models import Author, Book


def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {'authors': authors, 'books': books}
    return render(request, template_name='library/index.html', context=context)

def add_author(request):
    if request.method == "GET":
        author_form = AuthorForm()
        context = {"form": author_form}
        return render(request, template_name='library/add_author.html', context=context)

    if request.method == "POST":
        author_form = AuthorForm(data=request.POST)
        if author_form.is_valid():
            author = Author()
            author.name = author_form.cleaned_data['name']
            author.lastname = author_form.cleaned_data['lastname']
            author.patronymic = author_form.cleaned_data['patronymic']
            author.birthdate = author_form.cleaned_data['birthdate']
            author.save()
            return index(request)

def show_all_authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, template_name='library/author_list.html', context=context)

def add_book(request):
    if request.method == "GET":
        book_form = BookForm()
        context = {"form": book_form}
        return render(request, template_name='library/add_book.html', context=context)

    if request.method == "POST":
        book_form = BookForm(data=request.POST)
        if book_form.is_valid():
            book = Book()
            book.author = book_form.cleaned_data['author']
            book.title = book_form.cleaned_data['title']
            book.genre = book_form.cleaned_data['genre']
            book.written_in = book_form.cleaned_data['written_in']
            book.save()
            return index(request)

def show_all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template_name='library/book_list.html', context=context)
