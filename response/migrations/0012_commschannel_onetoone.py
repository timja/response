# Generated by Django 2.2.3 on 2019-10-24 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("response", "0011_auto_20190927_1339")]

    operations = [
        migrations.AlterField(
            model_name="commschannel",
            name="incident",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="response.Incident"
            ),
        )
    ]
