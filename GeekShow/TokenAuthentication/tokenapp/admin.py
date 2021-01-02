from django.contrib import admin

# Register your models here.
from .models import OdiBattingRecord

@admin.register(OdiBattingRecord)
class OdiRecordAdmin(admin.ModelAdmin):
    list_display = ['id','name','country','runs','fifties','centuries','double_centuries']