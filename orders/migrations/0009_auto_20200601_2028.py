# Generated by Django 3.0.6 on 2020-06-02 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_incart_p_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Product', verbose_name='product_id'),
        ),
    ]
