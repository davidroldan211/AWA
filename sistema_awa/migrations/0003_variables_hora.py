# Generated by Django 3.0.6 on 2020-07-09 05:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_awa', '0002_variables_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='variables',
            name='hora',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
