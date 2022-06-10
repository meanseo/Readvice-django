from django.db import models

class Book(models.Model):
    use_in_migrations = True
    book_id = models.AutoField(primary_key=True)
    isbn = models.CharField()
    book_title = models.TextField()
    author = models.TextField()
    book_info = models.TextField()
    library_name = models.DateField()
    price = models.DateField()
    category = models.DateField()

    class Meta:
        db_table = "books"

    def __str__(self):
        return f'{self.pk} {self.isbn}'