# Generated by Django 4.2.4 on 2023-09-02 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoBarras', models.CharField(default=0, max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('stock', models.PositiveBigIntegerField(default=0)),
                ('precio', models.PositiveBigIntegerField(default=0)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
    ]