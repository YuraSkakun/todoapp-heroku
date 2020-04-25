from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return "Профиль пользователя %s" % self.user.username
