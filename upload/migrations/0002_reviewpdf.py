# Generated by Django 4.2.6 on 2024-03-16 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("upload", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReviewPdf",
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
                    "marks",
                    models.BooleanField(
                        default=False, verbose_name="Marks by the editor/author."
                    ),
                ),
                (
                    "bibliographic_caption",
                    models.BooleanField(
                        default=False,
                        verbose_name="Bibliographic caption with journal information such as volume, number, supplement, special issue and year of publication.",
                    ),
                ),
                (
                    "table_of_contents",
                    models.BooleanField(
                        default=False,
                        verbose_name="For regular publication, Table of contents pagination matches the PDF.",
                    ),
                ),
                (
                    "pagination",
                    models.BooleanField(
                        default=False,
                        verbose_name="For AOP, Pagination appears as 1-X (it cannot have sequential pagination).",
                    ),
                ),
                (
                    "elocation",
                    models.BooleanField(
                        default=False,
                        verbose_name="For PC, Contains elocation-id (unique for each document) also optional pagination for 1-X printing (cannot have sequential pagination).",
                    ),
                ),
                (
                    "periodicity",
                    models.BooleanField(
                        default=False,
                        verbose_name="For regular publication, Periodicity information is included.",
                    ),
                ),
                (
                    "doi",
                    models.BooleanField(
                        default=False,
                        verbose_name="For all types of publication, DOI is included in the PDF (mandatory). The DOI number must be unique for each document.",
                    ),
                ),
                (
                    "doi_translation",
                    models.BooleanField(
                        default=False,
                        verbose_name="For all types of publication, When there is a translation if there is a different DOI for translation. If it appears in the PDF, it must be marked in the XML.",
                    ),
                ),
                (
                    "doi_characters",
                    models.BooleanField(
                        default=False,
                        verbose_name='There are no characters that could "break" the DOI registration in CrossRef.',
                    ),
                ),
                (
                    "license",
                    models.BooleanField(
                        default=False,
                        verbose_name="For all types of publication, Creative Commons (CC) license is included in the PDF (required).",
                    ),
                ),
                (
                    "history_dates",
                    models.BooleanField(
                        default=False,
                        verbose_name="For all types of publication, Articles that have undergone peer review must contain at least the complete history dates (day + month + year) of acceptance and approval.",
                    ),
                ),
                (
                    "label_affiliation",
                    models.BooleanField(
                        default=False,
                        verbose_name="For all modalities, Affiliation is correct and has its respective label between author and affiliation (mandatory).",
                    ),
                ),
                (
                    "orcid",
                    models.BooleanField(
                        default=False,
                        verbose_name="For all modalities, There is at least one author with ORCID (any author), if so, check if there is a visible number (In the model: 0000-0000-0000-0000 [allows letter]) or ORCID icon linked to the page from the author's ORCID.",
                    ),
                ),
                (
                    "taxonomy",
                    models.BooleanField(
                        default=False, verbose_name="Exists taxonomy information."
                    ),
                ),
                (
                    "role",
                    models.BooleanField(
                        default=False,
                        verbose_name="If there is an indication of author contributions, the marking in <role> is correct.",
                    ),
                ),
                (
                    "credit",
                    models.BooleanField(
                        default=False,
                        verbose_name="If Taxonomy CRediT, Tag attribute was marked correctly.",
                    ),
                ),
                (
                    "availability",
                    models.BooleanField(
                        default=False,
                        verbose_name="Data availability information has been marked with the correct tags.",
                    ),
                ),
                (
                    "opinion",
                    models.BooleanField(
                        default=False,
                        verbose_name="When an opinion is published, Marking follows guidelines and correct labeling.",
                    ),
                ),
                (
                    "preprint",
                    models.BooleanField(
                        default=False,
                        verbose_name="Preprint information was marked with the correct tags.",
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
                "abstract": False,
            },
        ),
    ]
