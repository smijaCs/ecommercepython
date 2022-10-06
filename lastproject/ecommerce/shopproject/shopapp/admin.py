from django.contrib import admin

# Register your models here.
from.models import category,product

class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(category,Categoryadmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','available','stock','created','update']
    list_editable = ['price','stock','available']
    prepopulated_fields ={'slug':('name',)}
    list_per_page=20
admin.site.register(product,ProductAdmin)