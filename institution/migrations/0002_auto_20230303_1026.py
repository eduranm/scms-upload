# Generated by Django 3.2.12 on 2023-03-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='acronym',
            field=models.TextField(blank=True, null=True, verbose_name='Institution Acronym'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='level_1',
            field=models.TextField(blank=True, null=True, verbose_name='Organization Level 1'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='level_2',
            field=models.TextField(blank=True, null=True, verbose_name='Organization Level 2'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='level_3',
            field=models.TextField(blank=True, null=True, verbose_name='Organization Level 3'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='Nome'),
        ),
    ]