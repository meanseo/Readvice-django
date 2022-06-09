from django.db import models

class User(models.Model):
    use_in_migrations = True
    username = models.CharField
    password = models.CharField
    name = models.TextField
    email = models.TextField
    regDate = models.TextField

    class Meta:
        db_table="users"

    def __str__(self):
        return f'{self.pk} {self.username}'