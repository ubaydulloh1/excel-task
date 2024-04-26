from celery import shared_task
from . import utils


@shared_task(name="update_products_task")
def update_products_task():
    utils.update_products()

    print("*=" * 200)
    print("==========       PRODUCTS UPDATED!          ==========")
    print("*=" * 200)


@shared_task(name="update_product_attributes_task")
def update_product_attributes():
    utils.update_shops()
    utils.update_brands()
    utils.update_product_categories()
    utils.update_measurement_units()

    print("*=" * 200)
    print("======           PRODUCT ATTRIBUTES UPDATED!            ")
    print("*=" * 200)
