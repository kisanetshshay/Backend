
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.URLField(help_text="Enter a real image URL (e.g., from Google Images or Unsplash)")

    def __str__(self):
        return self.name