# Generated by Django 4.2.7 on 2023-11-13 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'Неактивен'), ('ACTIVE', 'Активен')], max_length=32, verbose_name='Статус'),
        ),
    ]