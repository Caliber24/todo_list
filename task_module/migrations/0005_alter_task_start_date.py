# Generated by Django 5.1.3 on 2024-12-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_module', '0004_alter_task_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]