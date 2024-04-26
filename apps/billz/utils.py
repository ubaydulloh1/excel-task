import logging
from django.db import transaction

from . import services, models


@transaction.atomic
def update_product_categories():
    success, data = services.BillzApiService().fetch_product_categories()
    if not success:
        return

    try:
        categories = data["categories"]
    except KeyError:
        return

    remaining_ids = []
    for category in categories:
        cat_obj, _ = models.ProductCategory.objects.update_or_create(
            remote_id=category["id"],
            defaults={
                "name": category["name"],
                "parent_id": category["parent_id"],
                "is_open": category["is_open"],
            }
        )
        remaining_ids.append(cat_obj.id)

    models.ProductCategory.objects.exclude(id__in=remaining_ids).delete()


@transaction.atomic
def update_products():
    success, data = services.BillzApiService().fetch_products()
    if not success:
        return

    try:
        products = data["products"]
    except KeyError:
        return

    remaining_ids = []
    for product in products:
        measurement_unit, _ = models.MeasurementUnit.objects.update_or_create(
            remote_id=product["measurement_unit"]["id"],
            defaults={
                "name": product["measurement_unit"]["name"],
                "short_name": product["measurement_unit"]["short_name"],
            }
        )

        obj, _ = models.Product.objects.update_or_create(
            remote_id=product["id"],
            defaults={
                "name": product["name"],
                "parent_id": product["parent_id"],
                "brand_id": models.Brand.objects.get(remote_id=product["brand_id"]).id,
                "is_variative": product["is_variative"],
                "is_marked": product["is_marked"],
                "sku": product["sku"],
                "main_image": product["main_image_url"],
                "barcode": product["barcode"],
                "description": product["description"],
                "rmt_updated_at": product["updated_at"],
                "measurement_unit_id": measurement_unit.id,
                "type_id": product["product_type_id"],
            }
        )
        remaining_ids.append(obj.id)

        categories = product["categories"]
        attrs = product["product_attributes"]
        shop_prices = product["shop_prices"]

        # update product categories
        obj.categories.clear()
        cat_ids = []
        for cat in categories:
            cat_ids.append(cat["id"])

        obj.categories.add(*models.ProductCategory.objects.filter(remote_id__in=cat_ids))

        # update product attrs
        obj.attributes.clear()
        for attr in attrs:
            obj.attributes.add(
                models.ProductAttribute.objects.update_or_create(
                    remote_id=attr["attribute_id"],
                    defaults={
                        "value": attr["attribute_value"],
                    }
                )[0]
            )

        # update product shop prices
        obj.shop_prices.all().delete()
        for sh_price in shop_prices:
            shop, _ = models.Shop.objects.update_or_create(
                remote_id=sh_price["shop_id"],
                defaults={
                    "name": sh_price["shop_name"],
                }
            )
            obj.shop_prices.add(
                models.ProductShopPrice.objects.update_or_create(
                    shop_id=shop.id,
                    product_id=obj.id,
                    defaults={
                        "retail_price": sh_price["retail_price"],
                        "retail_currency": sh_price["retail_currency"],
                    }
                )[0]
            )

    models.Product.objects.exclude(id__in=remaining_ids).delete()


@transaction.atomic
def update_brands():
    success, data = services.BillzApiService().fetch_brands()
    if not success:
        return

    try:
        brands = data["brands"]
    except KeyError:
        return

    remaining_ids = []
    for brand in brands:
        obj, _ = models.Brand.objects.update_or_create(
            remote_id=brand["id"],
            defaults={
                "name": brand["name"],
                "company_id": brand["company_id"],
                "logo": brand["logo"],
            }
        )
        remaining_ids.append(obj.id)

    models.Brand.objects.exclude(id__in=remaining_ids).delete()


@transaction.atomic
def update_shops():
    success, data = services.BillzApiService().fetch_shops()
    if not success:
        return

    try:
        shops = data["shops"]
    except KeyError:
        return

    remaining_ids = []
    for shop in shops:
        obj, _ = models.Shop.objects.update_or_create(
            remote_id=shop["id"],
            defaults={
                "name": shop["name"],
                "company_id": shop["company_id"],
            }
        )
        remaining_ids.append(obj.id)

    models.Shop.objects.exclude(id__in=remaining_ids).delete()


@transaction.atomic
def update_measurement_units():
    pass
