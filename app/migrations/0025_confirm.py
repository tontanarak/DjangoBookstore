# Generated by Django 3.1.6 on 2021-02-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20210218_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='confirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('payID', models.CharField(max_length=300)),
                ('phoneNo', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300)),
            ],
        ),
    ]