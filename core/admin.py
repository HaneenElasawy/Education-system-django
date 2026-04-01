from django.contrib import admin
from .models import Student, Feedback , Subject , Grade , Profile

admin.site.register(Student)
admin.site.register(Feedback)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Profile)