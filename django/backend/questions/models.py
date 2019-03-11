from django.db import models
from django.urls import reverse


class Question(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('index')
