from django.contrib import admin

# Register your models here.
from .models import Product, Category, Processor, Videocard

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Processor)
admin.site.register(Videocard)