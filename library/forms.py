from django import forms

from .models import Author

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=200, label='Имя')
    lastname = forms.CharField(max_length=200, label='Фамилия')
    patronymic = forms.CharField(max_length=200, label='Отчество')
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'], label='Дата рождения')

class BookForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор')
    title = forms.CharField(max_length=200)
    genre = forms.CharField(max_length=200)
    written_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'], label='Год написания')
