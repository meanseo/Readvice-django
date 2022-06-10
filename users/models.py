from django.db import models

from django.db import models

class User(models.Model):
    use_in_migrations = True
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.TextField()
    regDate = models.DateField()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.username}'

class Comment(models.Model):
    use_in_migrations = True
    comment_id = models.AutoField(primary_key=True, max_length=10)
    comment = models.TextField()
    auto_recode = models.TextField()
    regDate = models.DateField()

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f'{self.pk} {self.comment_id}'

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
