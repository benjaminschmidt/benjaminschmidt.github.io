# Generated by Django 4.0.6 on 2022-10-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_alter_myself_professional_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]