# Generated by Django 4.1.1 on 2022-09-30 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_rate_rating_rate_range_rating_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0, max_length=1)),
            ],
        ),
    ]
