import openpyxl
from . import models
from django.db import transaction


@transaction.atomic
def import_lfl(excel, year, month) -> models.LFL:
    workbook = openpyxl.load_workbook(excel, data_only=True)
    worksheet = workbook["Sheet1"]

    total_row = worksheet[5]
    lfl = models.LFL(
        year=year,
        month=month,
        excel=excel,
        target=normalize_val(total_row[2].value),
        fact=normalize_val(total_row[4].value),
        performance=normalize_val(total_row[5].value, flt=True),
        deviation=normalize_val(total_row[6].value, flt=True),
        last_year_sales=normalize_val(total_row[7].value),
        comparison_with_last_month=normalize_val(total_row[8].value, flt=True),
        transactions=normalize_val(total_row[9].value),
        edn=normalize_val(total_row[10].value),
        traffic=normalize_val(total_row[11].value),
        last_months_traffic=normalize_val(total_row[12].value),
        comparison_of_traffic_with_last_month=normalize_val(total_row[13].value, flt=True),
        average_bill=normalize_val(total_row[14].value),
        average_price_of_goods_in_receipt=normalize_val(total_row[15].value),
        conversion=normalize_val(total_row[16].value, flt=True),
        average_quantity_of_goods_in_a_receipt=normalize_val(total_row[17].value),
        deviation_in_sums=normalize_val(total_row[20].value),
    )
    lfl.save()

    for index, row in enumerate(worksheet.iter_rows(values_only=True)):
        if index > 4 and row[0] is not None:
            lfl_daily = models.LFLDaily(
                lfl=lfl,
                date=row[1],
                target=normalize_val(row[2]),
                target_percent=normalize_val(row[3], flt=True),
                fact=normalize_val(row[4]),
                performance=normalize_val(row[5], flt=True),
                deviation=normalize_val(row[6], flt=True),
                last_year_sales=normalize_val(row[7]),
                comparison_with_last_month=normalize_val(row[8], flt=True),
                transactions=normalize_val(row[9]),
                edn=normalize_val(row[10]),
                traffic=normalize_val(row[11]),
                last_months_traffic=normalize_val(row[12]),
                comparison_of_traffic_with_last_month=normalize_val(row[13], flt=True),
                average_bill=normalize_val(row[14]),
                average_price_of_goods_in_receipt=normalize_val(row[15]),
                conversion=normalize_val(row[16], flt=True),
                average_quantity_of_goods_in_a_receipt=normalize_val(row[17]),
                comparison_from_last_week=normalize_val(row[18], flt=True),
                comparison_with_last_day=normalize_val(row[19], flt=True),
                deviation_in_sums=normalize_val(row[20]),
            )
            lfl_daily.save()
    return lfl


def normalize_val(val, flt=False) -> int | float | None:
    """ if flt is True than return float. """

    if not any([isinstance(val, int), isinstance(val, float)]):
        return None

    if flt:
        return round(val, 2) * 100
    return int(val)
