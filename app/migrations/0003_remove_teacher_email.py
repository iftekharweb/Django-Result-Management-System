# Generated by Django 5.0.3 on 2024-03-17 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_teacher_options_remove_teacher_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
    ]