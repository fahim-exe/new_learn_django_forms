from django.db import models

from django.core.validators import MaxLengthValidator, MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
