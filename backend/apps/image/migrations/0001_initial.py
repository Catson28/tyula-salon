# Generated by Django 4.2.9 on 2024-03-02 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("product", "__first__"),
        ("material", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                ("ImageID", models.AutoField(primary_key=True, serialize=False)),
                ("Path", models.CharField(max_length=255)),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        limit_choices_to={
                            "model__in": (
                                "product",
                                "materiaprima",
                                "cliente",
                                "profissional",
                                "user",
                            )
                        },
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RawMaterialImage",
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
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="img_raw_mat",
                        to="image.image",
                    ),
                ),
                (
                    "raw_material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="raw_mat_img",
                        to="material.rawmaterial",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="img_prod",
                        to="image.image",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prod_img",
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]
