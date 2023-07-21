# Generated by Django 4.2.1 on 2023-07-15 19:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pagetext",
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
                    "url_1",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_1",
                    models.CharField(
                        blank=True,
                        default="url_link_text_1",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_1",
                    models.CharField(
                        blank=True,
                        default="url_link_description_1",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_2",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_2",
                    models.CharField(
                        blank=True,
                        default="url_link_text_2",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_2",
                    models.CharField(
                        blank=True,
                        default="url_link_description_2",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_3",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_3",
                    models.CharField(
                        blank=True,
                        default="url_link_text_3",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_3",
                    models.CharField(
                        blank=True,
                        default="url_link_description_3",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_4",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_4",
                    models.CharField(
                        blank=True,
                        default="url_link_text_4",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_4",
                    models.CharField(
                        blank=True,
                        default="url_link_description_4",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_5",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_5",
                    models.CharField(
                        blank=True,
                        default="url_link_text_5",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_5",
                    models.CharField(
                        blank=True,
                        default="url_link_description_5",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_6",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_6",
                    models.CharField(
                        blank=True,
                        default="url_link_text_6",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_6",
                    models.CharField(
                        blank=True,
                        default="url_link_description_6",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_7",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_7",
                    models.CharField(
                        blank=True,
                        default="url_link_text_7",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_7",
                    models.CharField(
                        blank=True,
                        default="url_link_description_7",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_8",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_8",
                    models.CharField(
                        blank=True,
                        default="url_link_text_8",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_8",
                    models.CharField(
                        blank=True,
                        default="url_link_description_8",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_9",
                    models.URLField(
                        blank=True, default="https://chesnowitz.com/", null=True
                    ),
                ),
                (
                    "url_link_text_9",
                    models.CharField(
                        blank=True,
                        default="url_link_text_9",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "url_link_description_9",
                    models.CharField(
                        blank=True,
                        default="url_link_description_9",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "text_1",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_1", null=True
                    ),
                ),
                (
                    "text_2",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_2", null=True
                    ),
                ),
                (
                    "text_3",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_3", null=True
                    ),
                ),
                (
                    "text_4",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_4", null=True
                    ),
                ),
                (
                    "text_5",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_5", null=True
                    ),
                ),
                (
                    "text_6",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_6", null=True
                    ),
                ),
                (
                    "text_7",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_7", null=True
                    ),
                ),
                (
                    "text_8",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_8", null=True
                    ),
                ),
                (
                    "text_9",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_9", null=True
                    ),
                ),
                (
                    "text_10",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_10", null=True
                    ),
                ),
                (
                    "text_11",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_11", null=True
                    ),
                ),
                (
                    "text_12",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_12", null=True
                    ),
                ),
                (
                    "text_13",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_13", null=True
                    ),
                ),
                (
                    "text_14",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_14", null=True
                    ),
                ),
                (
                    "text_15",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_15", null=True
                    ),
                ),
                (
                    "text_16",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_16", null=True
                    ),
                ),
                (
                    "text_17",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_17", null=True
                    ),
                ),
                (
                    "text_18",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_18", null=True
                    ),
                ),
                (
                    "text_19",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_19", null=True
                    ),
                ),
                (
                    "text_20",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_20", null=True
                    ),
                ),
                (
                    "text_21",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_21", null=True
                    ),
                ),
                (
                    "text_22",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_22", null=True
                    ),
                ),
                (
                    "text_23",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_23", null=True
                    ),
                ),
                (
                    "text_24",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_24", null=True
                    ),
                ),
                (
                    "text_25",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_25", null=True
                    ),
                ),
                (
                    "text_26",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_26", null=True
                    ),
                ),
                (
                    "text_27",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_27", null=True
                    ),
                ),
                (
                    "text_28",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_28", null=True
                    ),
                ),
                (
                    "text_29",
                    ckeditor.fields.RichTextField(
                        blank=True, default="text_29", null=True
                    ),
                ),
                (
                    "char_1",
                    models.CharField(
                        blank=True, default="char_1", max_length=1000, null=True
                    ),
                ),
                (
                    "char_2",
                    models.CharField(
                        blank=True, default="char_2", max_length=1000, null=True
                    ),
                ),
                (
                    "char_3",
                    models.CharField(
                        blank=True, default="char_3", max_length=1000, null=True
                    ),
                ),
                (
                    "char_4",
                    models.CharField(
                        blank=True, default="char_4", max_length=1000, null=True
                    ),
                ),
                (
                    "char_5",
                    models.CharField(
                        blank=True, default="char_5", max_length=1000, null=True
                    ),
                ),
                (
                    "char_6",
                    models.CharField(
                        blank=True, default="char_6", max_length=1000, null=True
                    ),
                ),
                (
                    "char_7",
                    models.CharField(
                        blank=True, default="char_7", max_length=1000, null=True
                    ),
                ),
                (
                    "char_8",
                    models.CharField(
                        blank=True, default="char_8", max_length=1000, null=True
                    ),
                ),
                (
                    "char_9",
                    models.CharField(
                        blank=True, default="char_9", max_length=1000, null=True
                    ),
                ),
                (
                    "char_10",
                    models.CharField(
                        blank=True, default="char_10", max_length=1000, null=True
                    ),
                ),
                (
                    "char_11",
                    models.CharField(
                        blank=True, default="char_11", max_length=1000, null=True
                    ),
                ),
                (
                    "char_12",
                    models.CharField(
                        blank=True, default="char_12", max_length=1000, null=True
                    ),
                ),
                (
                    "char_13",
                    models.CharField(
                        blank=True, default="char_13", max_length=1000, null=True
                    ),
                ),
                (
                    "char_14",
                    models.CharField(
                        blank=True, default="char_14", max_length=1000, null=True
                    ),
                ),
                (
                    "char_15",
                    models.CharField(
                        blank=True, default="char_15", max_length=1000, null=True
                    ),
                ),
                (
                    "char_16",
                    models.CharField(
                        blank=True, default="char_16", max_length=1000, null=True
                    ),
                ),
                (
                    "char_17",
                    models.CharField(
                        blank=True, default="char_17", max_length=1000, null=True
                    ),
                ),
                (
                    "char_18",
                    models.CharField(
                        blank=True, default="char_18", max_length=1000, null=True
                    ),
                ),
                (
                    "char_19",
                    models.CharField(
                        blank=True, default="char_19", max_length=1000, null=True
                    ),
                ),
                (
                    "char_20",
                    models.CharField(
                        blank=True, default="char_20", max_length=1000, null=True
                    ),
                ),
                (
                    "char_21",
                    models.CharField(
                        blank=True, default="char_21", max_length=1000, null=True
                    ),
                ),
                (
                    "char_22",
                    models.CharField(
                        blank=True, default="char_22", max_length=1000, null=True
                    ),
                ),
                (
                    "char_23",
                    models.CharField(
                        blank=True, default="char_23", max_length=1000, null=True
                    ),
                ),
                (
                    "char_24",
                    models.CharField(
                        blank=True, default="char_24", max_length=1000, null=True
                    ),
                ),
                (
                    "char_25",
                    models.CharField(
                        blank=True, default="char_25", max_length=1000, null=True
                    ),
                ),
                (
                    "char_26",
                    models.CharField(
                        blank=True, default="char_26", max_length=1000, null=True
                    ),
                ),
                (
                    "char_27",
                    models.CharField(
                        blank=True, default="char_27", max_length=1000, null=True
                    ),
                ),
                (
                    "char_28",
                    models.CharField(
                        blank=True, default="char_28", max_length=1000, null=True
                    ),
                ),
                (
                    "char_29",
                    models.CharField(
                        blank=True, default="char_29", max_length=1000, null=True
                    ),
                ),
                ("bool_1", models.BooleanField(default=False)),
                ("bool_2", models.BooleanField(default=False)),
                ("bool_3", models.BooleanField(default=False)),
                ("bool_4", models.BooleanField(default=False)),
                ("bool_5", models.BooleanField(default=False)),
                ("bool_6", models.BooleanField(default=False)),
                ("bool_7", models.BooleanField(default=False)),
                ("bool_8", models.BooleanField(default=False)),
                ("bool_9", models.BooleanField(default=False)),
                ("bool_10", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "avatar",
                    models.ImageField(
                        default="default.jpg", upload_to="profile_images"
                    ),
                ),
                (
                    "open_api_key",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                ("use_light_theme", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
