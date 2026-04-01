from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    email = models.EmailField()
    image = models.ImageField(upload_to='students/')
    slug = models.SlugField( unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.email

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)    
    description = models.TextField()
    slug = models.SlugField( unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def _str_(self):
        return f"{self.student.name} - {self.subject.name} - {self.score}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def _str_(self):
        return self.user.username        