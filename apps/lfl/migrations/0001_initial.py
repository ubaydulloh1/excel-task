# Generated by Django 5.0.4 on 2024-04-23 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LFL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('month', models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('excel', models.FileField(upload_to='')),
                ('target', models.BigIntegerField(help_text='uzbek sum')),
                ('fact', models.BigIntegerField(help_text='uzbek sum')),
                ('performance', models.BigIntegerField()),
                ('deviation', models.BigIntegerField()),
                ('last_year_sales', models.BigIntegerField()),
                ('comparison_with_last_month', models.DecimalField(decimal_places=2, max_digits=5)),
                ('transactions', models.IntegerField()),
                ('edn', models.IntegerField()),
                ('traffic', models.IntegerField()),
                ('last_months_traffic', models.IntegerField()),
                ('comparison_of_traffic_with_last_month', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_bill', models.IntegerField()),
                ('average_price_of_goods_in_receipt', models.IntegerField()),
                ('conversion', models.DecimalField(decimal_places=5, max_digits=5)),
                ('average_quantity_of_goods_in_a_receipt', models.DecimalField(decimal_places=5, max_digits=5)),
                ('deviation_in_sums', models.BigIntegerField()),
            ],
            options={
                'db_table': 'lfl',
            },
        ),
        migrations.CreateModel(
            name='LFLDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('target', models.BigIntegerField(help_text='uzbek sum')),
                ('fact', models.BigIntegerField(help_text='uzbek sum', null=True)),
                ('performance', models.BigIntegerField(null=True)),
                ('deviation', models.BigIntegerField()),
                ('last_year_sales', models.BigIntegerField()),
                ('comparison_with_last_month', models.DecimalField(decimal_places=2, max_digits=5)),
                ('transactions', models.IntegerField(null=True)),
                ('edn', models.IntegerField(null=True)),
                ('traffic', models.IntegerField(null=True)),
                ('last_months_traffic', models.IntegerField(null=True)),
                ('comparison_of_traffic_with_last_month', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_bill', models.IntegerField(null=True)),
                ('average_price_of_goods_in_receipt', models.IntegerField(null=True)),
                ('conversion', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('average_quantity_of_goods_in_a_receipt', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('comparison_from_last_week', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comparison_with_last_day', models.DecimalField(decimal_places=2, max_digits=5)),
                ('deviation_in_sums', models.BigIntegerField()),
                ('lfl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='lfl.lfl')),
            ],
            options={
                'db_table': 'lfl_daily',
            },
        ),
    ]
