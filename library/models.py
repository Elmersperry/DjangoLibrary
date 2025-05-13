from django.db import models

class Author(models.Model):
    # name
    # lastname
    # patronymic
    # birthdate
    pass

class Book(models.Model):
    # author(foreignkey)
    # title
    # genre
    # written_in(date of creation of book)
    pass