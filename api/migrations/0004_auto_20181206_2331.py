# Generated by Django 2.1.2 on 2018-12-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181206_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distances',
            name='map_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='distances',
            name='point_A',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='distances',
            name='point_B',
            field=models.CharField(max_length=150),
        ),
    ]
