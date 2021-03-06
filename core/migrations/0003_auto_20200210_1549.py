# Generated by Django 3.0.3 on 2020-02-10 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_proprietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Marca'),
        ),
    ]
