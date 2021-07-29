from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from django.contrib.auth import get_user_model
# User = get_user_model()


class Schools(models.Model):
    user = models.CharField(max_length=200)
    school = models.CharField(max_length=200)

    def __str__(self):
        return self.user + ':' + self.school

class Classes(models.Model):
    user = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    capasity = models.IntegerField()

    def __str__(self):
        return self.user + ':' + self.school

class Table(models.Model):
    user = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    num_of_session = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    first_day = models.CharField(max_length=200)
    second_day = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    signup_capasity = models.CharField(max_length=200)
