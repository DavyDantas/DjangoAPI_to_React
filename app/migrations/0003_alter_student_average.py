# Generated by Django 5.0.3 on 2024-03-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='average',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
