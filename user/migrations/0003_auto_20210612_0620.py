# Generated by Django 3.2.4 on 2021-06-12 06:20

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_created_at'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TextField(default=1623478799.8250213),
        ),
    ]