# Generated by Django 3.2.9 on 2021-11-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]