# Generated by Django 5.1.2 on 2024-10-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]