# Generated by Django 4.2.7 on 2024-05-07 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_token_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Token',
        ),
    ]
