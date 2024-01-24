# Generated by Django 4.2.6 on 2024-01-23 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("journal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "publication_initial_month_number",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "JANUARY"),
                            (2, "FEBRUARY"),
                            (3, "MARCH"),
                            (4, "APRIL"),
                            (5, "MAY"),
                            (6, "JUNE"),
                            (7, "JULY"),
                            (8, "AUGUST"),
                            (9, "SEPTEMBER"),
                            (10, "OCTOBER"),
                            (11, "NOVEMBER"),
                            (12, "DECEMBER"),
                        ],
                        null=True,
                        verbose_name="Publication initial month number",
                    ),
                ),
                (
                    "publication_initial_month_name",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Publication initial month name",
                    ),
                ),
                (
                    "publication_final_month_number",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "JANUARY"),
                            (2, "FEBRUARY"),
                            (3, "MARCH"),
                            (4, "APRIL"),
                            (5, "MAY"),
                            (6, "JUNE"),
                            (7, "JULY"),
                            (8, "AUGUST"),
                            (9, "SEPTEMBER"),
                            (10, "OCTOBER"),
                            (11, "NOVEMBER"),
                            (12, "DECEMBER"),
                        ],
                        null=True,
                        verbose_name="Publication final month number",
                    ),
                ),
                (
                    "publication_final_month_name",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Publication final month name",
                    ),
                ),
                (
                    "publication_date_text",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Publication date text"
                    ),
                ),
                (
                    "volume",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="Volume"
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="Number"
                    ),
                ),
                (
                    "supplement",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="Supplement"
                    ),
                ),
                (
                    "publication_year",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="Year"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "journal",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="journal.journal",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["journal"], name="issue_issue_journal_dcc9f6_idx"
                    ),
                    models.Index(
                        fields=["publication_year"],
                        name="issue_issue_publica_a3a5c7_idx",
                    ),
                    models.Index(
                        fields=["volume"], name="issue_issue_volume_71bce1_idx"
                    ),
                    models.Index(
                        fields=["number"], name="issue_issue_number_780a64_idx"
                    ),
                    models.Index(
                        fields=["supplement"], name="issue_issue_supplem_bd88be_idx"
                    ),
                ],
                "unique_together": {
                    ("journal", "publication_year", "volume", "number", "supplement"),
                    ("journal", "volume", "number", "supplement"),
                },
            },
        ),
    ]
