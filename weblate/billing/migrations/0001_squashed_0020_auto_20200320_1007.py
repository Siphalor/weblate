# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.5 on 2020-04-16 11:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import weblate.utils.fields


class Migration(migrations.Migration):
    replaces = [
        ("billing", "0001_squashed_0016_remove_billing_user"),
        ("billing", "0002_auto_20180905_1400"),
        ("billing", "0003_billing_owners"),
        ("billing", "0004_auto_20181021_1249"),
        ("billing", "0005_auto_20181021_1254"),
        ("billing", "0006_auto_20181021_1256"),
        ("billing", "0007_plan_public"),
        ("billing", "0008_auto_20181024_1151"),
        ("billing", "0009_auto_20181101_0900"),
        ("billing", "0010_invoice_amount"),
        ("billing", "0011_billing_grace_period"),
        ("billing", "0012_auto_20181207_0843"),
        ("billing", "0013_auto_20190208_1452"),
        ("billing", "0014_billing_removal"),
        ("billing", "0015_auto_20190516_1159"),
        ("billing", "0016_auto_20190911_1316"),
        ("billing", "0017_auto_20190919_1101"),
        ("billing", "0018_plan_slug"),
        ("billing", "0019_slugify"),
        ("billing", "0020_auto_20200320_1007"),
    ]

    initial = True

    dependencies = [
        ("trans", "0001_squashed_0143_auto_20180609_1655"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("price", models.IntegerField(default=0)),
                ("limit_strings", models.IntegerField(default=0)),
                ("limit_languages", models.IntegerField(default=0)),
                ("limit_projects", models.IntegerField(default=0)),
                ("yearly_price", models.IntegerField(default=0)),
                ("display_limit_languages", models.IntegerField(default=0)),
                ("display_limit_projects", models.IntegerField(default=0)),
                ("display_limit_strings", models.IntegerField(default=0)),
                ("change_access_control", models.BooleanField(default=True)),
                ("public", models.BooleanField(default=False)),
                ("slug", models.SlugField(max_length=100, unique=True)),
            ],
            options={},
        ),
        migrations.CreateModel(
            name="Billing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billing.Plan",
                        verbose_name="Billing plan",
                    ),
                ),
                (
                    "projects",
                    models.ManyToManyField(
                        blank=True, to="trans.Project", verbose_name="Billed projects"
                    ),
                ),
                (
                    "state",
                    models.IntegerField(
                        choices=[
                            (0, "Active"),
                            (1, "Trial"),
                            (2, "Expired"),
                            (3, "Terminated"),
                        ],
                        default=0,
                        verbose_name="Billing state",
                    ),
                ),
                (
                    "in_limits",
                    models.BooleanField(
                        default=True, editable=False, verbose_name="In limits"
                    ),
                ),
                (
                    "paid",
                    models.BooleanField(
                        default=True, editable=False, verbose_name="Paid"
                    ),
                ),
                (
                    "expiry",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        help_text="After expiry removal with 15 days grace period is scheduled.",
                        null=True,
                        verbose_name="Trial expiry date",
                    ),
                ),
                (
                    "owners",
                    models.ManyToManyField(
                        blank=True,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Billing owners",
                    ),
                ),
                ("payment", weblate.utils.fields.JSONField(default={}, editable=False)),
                (
                    "grace_period",
                    models.IntegerField(
                        default=0, verbose_name="Grace period for payments"
                    ),
                ),
                (
                    "removal",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        help_text="This is automatically set after trial expiry.",
                        null=True,
                        verbose_name="Scheduled removal",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start", models.DateField()),
                ("end", models.DateField()),
                ("payment", weblate.utils.fields.JSONField(default={}, editable=False)),
                (
                    "currency",
                    models.IntegerField(
                        choices=[(0, "EUR"), (1, "mBTC"), (2, "USD"), (3, "CZK")],
                        default=0,
                    ),
                ),
                ("ref", models.CharField(blank=True, max_length=50)),
                ("note", models.TextField(blank=True)),
                (
                    "billing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billing.Billing",
                    ),
                ),
                ("amount", models.FloatField()),
            ],
            options={},
        ),
    ]
