# Generated by Django 2.2.5 on 2019-09-24 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20190924_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelimage',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.TravelRecord', verbose_name='Путешествие'),
        ),
    ]
