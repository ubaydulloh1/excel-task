# Generated by Django 5.0.4 on 2024-04-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remote_id', models.UUIDField(help_text='billz id', unique=True)),
                ('value', models.CharField()),
            ],
            options={
                'verbose_name': 'Product attribute',
                'verbose_name_plural': 'Product attributes',
                'db_table': 'billz_product_attribute',
            },
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product category', 'verbose_name_plural': 'Product categories'},
        ),
        migrations.AlterModelOptions(
            name='productshopprice',
            options={'verbose_name': 'Product shop price', 'verbose_name_plural': 'Product shop prices'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(blank=True, related_name='products', to='billz.productattribute'),
        ),
    ]
