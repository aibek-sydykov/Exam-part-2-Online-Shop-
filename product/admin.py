from django.contrib import admin
from product.models import Product, Category


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
