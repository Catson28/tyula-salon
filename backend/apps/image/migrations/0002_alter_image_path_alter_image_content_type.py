# Generated by Django 4.2.9 on 2024-03-10 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("image", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="Path",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="image",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
    ]
