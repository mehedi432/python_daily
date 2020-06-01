from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/images/')
    title = models.CharField(max_length=233)
    description = models.CharField(max_length=377)
    url = models.URLField(blank=True)
