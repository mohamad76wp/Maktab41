# Generated by Django 3.1.4 on 2021-02-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Payment Status'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
    ]
