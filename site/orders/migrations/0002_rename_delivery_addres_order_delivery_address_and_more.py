# Generated by Django 4.2.16 on 2024-12-05 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_addres',
            new_name='delivery_address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='peyment_on_get',
            new_name='payment_on_get',
        ),
    ]
