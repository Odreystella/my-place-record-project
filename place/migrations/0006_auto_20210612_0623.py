# Generated by Django 3.2.4 on 2021-06-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_auto_20210612_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1623478991.4551878),
        ),
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.TextField(default=1623478991.4551878),
        ),
    ]
