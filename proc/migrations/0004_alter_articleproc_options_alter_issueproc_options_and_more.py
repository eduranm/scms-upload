# Generated by Django 5.0.3 on 2024-03-29 17:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("proc", "0003_procreport_item_type_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="articleproc",
            options={"ordering": ["-updated"]},
        ),
        migrations.AlterModelOptions(
            name="issueproc",
            options={"ordering": ["-updated"]},
        ),
        migrations.AlterModelOptions(
            name="journalproc",
            options={"ordering": ["-updated"]},
        ),
        migrations.AlterModelOptions(
            name="operation",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterModelOptions(
            name="procreport",
            options={
                "ordering": ["-created"],
                "verbose_name": "Processing report",
                "verbose_name_plural": "Processing reports",
            },
        ),
    ]
