# Generated by Django 2.1.7 on 2019-02-16 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gcvClassification', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='products',
            new_name='Product',
        ),
    ]