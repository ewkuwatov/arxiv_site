# Generated by Django 4.2.3 on 2024-10-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiveapp', '0004_essay_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10000, max_digits=10),
        ),
    ]
