# Generated by Django 3.0.3 on 2020-02-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_mensalista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalista',
            name='inicio',
            field=models.DateField(),
        ),
    ]
