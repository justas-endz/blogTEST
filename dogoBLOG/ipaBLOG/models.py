from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now=True)
    content = HTMLField()
    objects = models.Manager()
    id = models.BigAutoField(primary_key=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

# class Comments(models.Model):
