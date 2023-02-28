from django.db import models

class Manga(models.Model):
    last = models.CharField(max_length=8)

    def __str__(self):
        return self.last