# Generated by Django 3.2.4 on 2021-06-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20210609_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1623238500.8802452),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.TextField(default=1623238500.8802452),
        ),
    ]
