# Generated by Django 2.2.5 on 2019-09-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20190924_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelrecord',
            name='place_name',
            field=models.CharField(default='Tomsk', max_length=300, verbose_name='Название места'),
            preserve_default=False,
        ),
    ]
