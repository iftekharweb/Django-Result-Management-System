# Generated by Django 5.0.3 on 2024-03-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_student_semester_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='attendence_marks',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='mark',
            name='ct_marks',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='mark',
            name='presentation_marks',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='mark',
            name='semester_final_marks',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
