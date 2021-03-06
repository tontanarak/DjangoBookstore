# Generated by Django 3.1.6 on 2021-02-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_book_bookpic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='AddressID',
        ),
        migrations.AddField(
            model_name='payment',
            name='Address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='BookID',
            field=models.ManyToManyField(to='app.Book'),
        ),
        migrations.AddField(
            model_name='payment',
            name='BookQty',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='Status',
            field=models.CharField(choices=[('W', 'Waiting'), ('C', 'Cancel'), ('D', 'Done')], default='W', max_length=1),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
