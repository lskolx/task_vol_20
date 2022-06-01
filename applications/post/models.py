from django.db import models

from applications.category.models import Category
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    text = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"{self.title} - Date: {self.created_at}"

