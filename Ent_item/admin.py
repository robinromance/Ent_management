from django.contrib import admin
from Ent_item.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = 'id', 's_name', 's_class', 's_address'

admin.site.register(Student, StudentAdmin)
