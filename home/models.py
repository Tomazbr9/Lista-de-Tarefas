from django.db import models
from django.contrib.auth.models import User


class ListModel(models.Model):
    show = models.BooleanField(default=False)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
