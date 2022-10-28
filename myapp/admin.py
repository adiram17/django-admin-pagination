from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'year')
    list_per_page = 5 # No of records per page 
    

admin.site.register(Book, BookAdmin)