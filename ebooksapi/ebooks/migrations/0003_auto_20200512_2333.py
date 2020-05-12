# Generated by Django 3.0.6 on 2020-05-12 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0002_auto_20200512_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_author',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]