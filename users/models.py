from django.db import models

class User(models.Model):
    use_in_migrations = True
    email = models.TextField(primary_key=True)
    password = models.CharField(max_length=10)
    username = models.TextField()
    birth = models.TextField()
    gender = models.TextField()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.email}'