# Generated by Django 3.0.6 on 2020-06-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incart',
            old_name='customer_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='incart',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=0),
        ),
    ]