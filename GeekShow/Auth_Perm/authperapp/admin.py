from django.contrib import admin

# Register your models here.
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','city','post','salary']