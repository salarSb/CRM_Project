# Generated by Django 3.2.5 on 2021-07-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_quoteitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteitem',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]