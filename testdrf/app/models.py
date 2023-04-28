from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    def __str__(self):
        return '%s : %s' % (self.key, self.value)



class Entity(models.Model):
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    properties = models.ManyToManyField('Property')


