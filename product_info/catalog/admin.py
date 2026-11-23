from django.contrib import admin
from .models import Category, Tag, Product

# Register your models here.
# Including all three models so we can easily create all three types in admin
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)