# Generated by Django 5.0.4 on 2024-04-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lfl', '0003_lfldaily_target_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lfl',
            name='deviation',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfl',
            name='performance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='comparison_from_last_week',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='comparison_of_traffic_with_last_month',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='comparison_with_last_day',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='comparison_with_last_month',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='deviation',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='deviation_in_sums',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='last_year_sales',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='performance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lfldaily',
            name='target',
            field=models.BigIntegerField(help_text='uzbek sum', null=True),
        ),
    ]
