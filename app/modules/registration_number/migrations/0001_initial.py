# Generated by Django 4.2.7 on 2023-11-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CounterModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Название счетчика')),
                ('current_no', models.IntegerField(verbose_name='Сквозной номер')),
                ('yearly_current_no', models.IntegerField(verbose_name='Сквозной номер за год')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
