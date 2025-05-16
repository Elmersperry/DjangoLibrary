from django.db import models

class Author(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name="Имя")
    lastname = models.TextField(null=True, blank=True, verbose_name="Фамилия")
    patronymic = models.TextField(null=True, blank=True, verbose_name="Отчество")
    birthdate = models.DateTimeField()

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.TextField(max_length=200, verbose_name='Назавание', null=True)
    genre = models.TextField(max_length=200, verbose_name='Жанр', null=True)
    written_in = models.DateTimeField()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title