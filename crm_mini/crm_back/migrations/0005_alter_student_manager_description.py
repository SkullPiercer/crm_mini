# Generated by Django 4.2.16 on 2024-09-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_back', '0004_alter_student_recommended_direction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='manager_description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
