from django.db import models

class Quote(models.Model):
    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    weight = models.PositiveIntegerField(default=1)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.text} — {self.author}"