# Generated by Django 4.2.7 on 2023-11-17 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationNumberModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=64, verbose_name='Регистрационный номер')),
                ('rent_timestamp', models.DateTimeField(verbose_name='Дата аренды')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]