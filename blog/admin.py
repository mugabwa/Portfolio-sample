from django.contrib import admin
from .models import Category, Post

# Register your models here.
## Used to customize what is shown on the admin pages
class PostAdmin(admin.ModelAdmin):
    pass

## Used to customize what is shown on the admin pages
class CategoryAdmin(admin.ModelAdmin):
    pass

## Include the tables in the admin interface
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)