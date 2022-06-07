# Generated by Django 3.0 on 2022-06-06 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_invoice_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
