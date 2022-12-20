from django.db import models


class UserModel(models.Model):
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=20)

    # def __str__(self):
    #     return f"User: {self.username}"
