from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=233)
    description = models.TextField()
    date = models.DateField()
    