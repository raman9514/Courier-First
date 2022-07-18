# Generated by Django 3.2.9 on 2021-11-23 16:41

import OrderApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0002_auto_20210417_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdb',
            name='delivery_phone',
            field=models.IntegerField(validators=[OrderApp.models.validatephone]),
        ),
        migrations.AlterField(
            model_name='orderdb',
            name='delivery_pincode',
            field=models.IntegerField(validators=[OrderApp.models.validatepincode]),
        ),
        migrations.AlterField(
            model_name='orderdb',
            name='pick_phone',
            field=models.IntegerField(validators=[OrderApp.models.validatephone]),
        ),
        migrations.AlterField(
            model_name='orderdb',
            name='pick_pincode',
            field=models.IntegerField(validators=[OrderApp.models.validatepincode]),
        ),
    ]
