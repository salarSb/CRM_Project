# Generated by Django 3.2.5 on 2021-08-06 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20210724_1927'),
        ('sale', '0011_auto_20210806_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizations.organization'),
        ),
    ]
