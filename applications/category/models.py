from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.title}"

