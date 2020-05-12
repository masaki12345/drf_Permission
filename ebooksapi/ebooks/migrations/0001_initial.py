# Generated by Django 3.0.6 on 2020-05-12 13:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('review_author', models.TextField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(5)])),
                ('ebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ebooks.Ebook')),
            ],
        ),
    ]