# Generated by Django 4.2.7 on 2023-11-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('status', models.IntegerField(choices=[(0, 'Неактивен'), (1, 'Активен')], verbose_name='Статус')),
                ('is_hidden', models.BooleanField(verbose_name='показывать')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
