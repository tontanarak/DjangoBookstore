# Generated by Django 3.1.6 on 2021-02-18 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20210218_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='books',
            new_name='BookID',
        ),
    ]
