from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    email = models.EmailField()
    image = models.ImageField(upload_to='students/')

    def _str_(self):
        return self.name


class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.email