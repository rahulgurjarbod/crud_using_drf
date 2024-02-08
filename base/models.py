from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    rollNo = models.IntegerField()
    section = models.CharField(max_length=100, blank=True, null=True)
    phoneNo = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name