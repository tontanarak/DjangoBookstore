# Generated by Django 3.1.6 on 2021-02-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210217_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='BookPic',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]