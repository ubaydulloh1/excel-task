from django.db import models


class MonthChoices(models.IntegerChoices):
    JANUARY = 1, "January"
    FEBRUARY = 2, "February"
    MARCH = 3, "March"
    APRIL = 4, "April"
    MAY = 5, "May"
    JUNE = 6, "June"
    JULY = 7, "July"
    AUGUST = 8, "August"
    SEPTEMBER = 9, "September"
    OCTOBER = 10, "October"
    NOVEMBER = 11, "November"
    DECEMBER = 12, "December"


class LFL(models.Model):
    class Meta:
        db_table = "lfl"

    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField(choices=MonthChoices.choices)
    excel = models.FileField()

    target = models.BigIntegerField(help_text="uzbek sum")
    fact = models.BigIntegerField(help_text="uzbek sum")
    performance = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    deviation = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    last_year_sales = models.BigIntegerField()
    comparison_with_last_month = models.DecimalField(decimal_places=2, max_digits=5)
    transactions = models.IntegerField()
    edn = models.IntegerField()
    traffic = models.IntegerField()
    last_months_traffic = models.IntegerField()
    comparison_of_traffic_with_last_month = models.DecimalField(max_digits=5, decimal_places=2)
    average_bill = models.IntegerField()
    average_price_of_goods_in_receipt = models.IntegerField()
    conversion = models.DecimalField(decimal_places=2, max_digits=5)
    average_quantity_of_goods_in_a_receipt = models.DecimalField(decimal_places=2, max_digits=5)
    deviation_in_sums = models.BigIntegerField()

    def __str__(self):
        return f"{self.year}, {self.get_month_display()}"


class LFLDaily(models.Model):
    class Meta:
        db_table = "lfl_daily"

    lfl = models.ForeignKey(to="LFL", on_delete=models.CASCADE, related_name="days")
    date = models.DateField()

    target = models.BigIntegerField(help_text="uzbek sum", null=True)
    target_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fact = models.BigIntegerField(help_text="uzbek sum", null=True)
    performance = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    deviation = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    last_year_sales = models.BigIntegerField(null=True)
    comparison_with_last_month = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    transactions = models.IntegerField(null=True)
    edn = models.IntegerField(null=True)
    traffic = models.IntegerField(null=True)
    last_months_traffic = models.IntegerField(null=True)
    comparison_of_traffic_with_last_month = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    average_bill = models.IntegerField(null=True)
    average_price_of_goods_in_receipt = models.IntegerField(null=True)
    conversion = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    average_quantity_of_goods_in_a_receipt = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    comparison_from_last_week = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    comparison_with_last_day = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    deviation_in_sums = models.BigIntegerField(null=True)

    def __str__(self):
        return f"{self.lfl}, {self.date}"
