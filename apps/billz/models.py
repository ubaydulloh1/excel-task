from django.db import models
from apps.common.models import BaseModel


class BillzBaseModel(BaseModel):
    class Meta:
        abstract = True

    remote_id = models.UUIDField(help_text="billz id", unique=True)


class ProductCategory(BillzBaseModel):
    class Meta:
        db_table = "billz_product_category"
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to="self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)
    is_open = models.BooleanField()

    def __str__(self):
        return self.name


class Product(BillzBaseModel):
    class Meta:
        db_table = "billz_product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    parent = models.ForeignKey(to="self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)
    brand = models.ForeignKey(to="Brand", on_delete=models.CASCADE, related_name="products")
    categories = models.ManyToManyField(to="ProductCategory", related_name="products", blank=True)
    measurement_unit = models.ForeignKey(
        to="MeasurementUnit", on_delete=models.SET_NULL, related_name="products", null=True
    )

    name = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to="billz/products/")
    type_id = models.UUIDField()
    barcode = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    is_variative = models.BooleanField()
    rmt_updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Brand(BillzBaseModel):
    class Meta:
        db_table = "billz_brand"
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    company_id = models.UUIDField()
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="billz/brands/")

    def __str__(self):
        return self.name


class MeasurementUnit(BillzBaseModel):
    class Meta:
        db_table = "billz_measurement_unit"
        verbose_name = "Product measurement unit"
        verbose_name_plural = "Product measurement units"

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}({self.short_name})"


class Shop(BillzBaseModel):
    class Meta:
        db_table = "billz_shop"
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    company_id = models.UUIDField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductShopPrice(BillzBaseModel):
    class Meta:
        db_table = "billz_product_shop_price"
        verbose_name = "Product shop price"
        verbose_name_plural = "Product shop prices"

    shop = models.ForeignKey(to="Shop", on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE, related_name="shop_prices")
    retail_price = models.DecimalField(max_digits=20, decimal_places=2)
    retail_currency = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.shop} - {self.product}"
