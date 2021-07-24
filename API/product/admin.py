from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','pname', 'pprice', 'description','category','account')

    class Meta:
        Ordering =["id"]
admin.site.register(Product, ProductAdmin)