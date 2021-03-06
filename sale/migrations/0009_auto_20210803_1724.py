# Generated by Django 3.2.5 on 2021-08-03 12:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20210724_1927'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sale', '0008_remove_quoteitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteitem',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('D', 'done'), ('F', 'failed')], max_length=1)),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizations.organization')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
