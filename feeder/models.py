from django.db import models


# Create your models here.
class Galileo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=85)


class Feeder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=85)
    galileo = models.ForeignKey(Galileo, on_delete=models.CASCADE)


class Credential(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=85)
    password = models.CharField(max_length=85)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=85)
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE)
