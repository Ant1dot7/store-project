from django.contrib import admin

from .models import *


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity',)
    extra = 0
