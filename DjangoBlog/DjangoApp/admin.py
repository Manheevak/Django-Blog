from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','date','title') 
    search_fields = ['title']
    readonly_fields = ['date']
