from django.contrib import admin
from .models import Subject,department,Type,Student,Faculty,Complaint


# Register your models here.
admin.site.register(Subject)
admin.site.register(department)
admin.site.register(Type)
admin.site.register(Student)
admin.site.register(Faculty)
# admin.site.register(HOD)
admin.site.register(Complaint)

