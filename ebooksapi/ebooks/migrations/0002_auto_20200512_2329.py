# Generated by Django 3.0.6 on 2020-05-12 14:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewsss', to='ebooks.Ebook'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)]),
        ),
    ]
