# Generated by Django 3.2.12 on 2022-07-28 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Package File')),
                ('signature', models.CharField(blank=True, max_length=32, null=True, verbose_name='Signature')),
                ('status', models.PositiveSmallIntegerField(choices=[('1', 'Submetido'), ('2', 'Finished')], default='1', verbose_name='Status')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='package_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'permissions': (('finish_deposit', 'Can finish deposit'),),
            },
        ),
    ]
