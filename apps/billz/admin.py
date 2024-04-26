from django.contrib import admin

from . import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductShopPrice)
class ProductShopPriceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasurementUnit)
class MeasurementUnitAdmin(admin.ModelAdmin):
    pass
