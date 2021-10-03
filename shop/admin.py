from django.contrib import admin
from shop.models import Category, Product, Image

admin.site.register(Image)
admin.site.empty_value_display = '✖'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('id',)
    list_display = ('name', 'show_available')

    def show_available(self, obj):
        if obj.is_available is True:
            return '✖'
        return '✓'
    show_available.short_description = 'Скрыт'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    extend = ('id',)
    list_display = ('name', 'show_price', 'show_available')

    def show_available(self, obj):
        if obj.is_available > 0:
            return '✓'
        return '✖'
    show_available.short_description = 'В продаже'
