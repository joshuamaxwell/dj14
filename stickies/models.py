from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    text = models.TextField()
    color = models.CharField(max_length=16, default="#ffff00")
    user = models.ForeignKey(User)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s "%(self.text)