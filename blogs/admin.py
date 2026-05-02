from django.contrib import admin
from .models import Category, Blog

# Display table of the blog
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # list of table
    list_display = ("title", "category", "author", "status", "is_featured")
    # search function for the UI
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


# Register your models here.

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
