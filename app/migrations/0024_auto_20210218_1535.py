# Generated by Django 3.1.6 on 2021-02-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_payment_bookid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Status',
            field=models.CharField(choices=[('Waiting', 'Waiting'), ('Cancel', 'Cancel'), ('Done', 'Done')], default='Waiting', max_length=10),
        ),
    ]
