# Generated by Django 4.2.9 on 2024-03-01 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
        ("customer", "0001_initial"),
        ("sale", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale_prodsal",
                        to="product.product",
                    ),
                ),
                (
                    "sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prodsal_sale",
                        to="sale.sale",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClientSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale_clisal",
                        to="customer.customer",
                    ),
                ),
                (
                    "sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clisal_sale",
                        to="sale.sale",
                    ),
                ),
            ],
        ),
    ]