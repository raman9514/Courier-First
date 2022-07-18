# Generated by Django 3.1.7 on 2021-04-17 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OrderApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdb',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderdb',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedbackdb',
            name='order_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='OrderApp.orderdb'),
        ),
    ]