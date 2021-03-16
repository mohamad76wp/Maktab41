# Generated by Django 3.1.7 on 2021-03-12 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210222_0723'),
        ('orders', '0002_auto_20210209_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='shop_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='basket_item', related_query_name='basket_item', to='products.shopproduct', verbose_name='shop_product'),
        ),
    ]