# Generated by Django 2.2.5 on 2019-09-24 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20190924_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelimage',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel_images', to='map.TravelRecord', verbose_name='Путешествие'),
        ),
    ]
