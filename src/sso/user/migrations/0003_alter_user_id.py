# Generated by Django 4.1 on 2022-08-20 18:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('976c4fdf-f124-49a0-bb72-d5a920a924e3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
