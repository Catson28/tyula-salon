# Generated by Django 4.2.9 on 2024-03-09 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("service", "0001_initial"),
        ("customer", "__first__"),
        ("professional", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
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
                ("payment_type", models.CharField(max_length=100)),
                ("date_time", models.DateTimeField()),
                (
                    "alternative_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cust_sale",
                        to="customer.customer",
                    ),
                ),
                (
                    "professional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profess_sale",
                        to="professional.professional",
                    ),
                ),
                ("services", models.ManyToManyField(to="service.service")),
            ],
        ),
        migrations.CreateModel(
            name="ServiceSale",
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
                    "sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="servsal_sale",
                        to="sale.sale",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale_servsal",
                        to="service.service",
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
