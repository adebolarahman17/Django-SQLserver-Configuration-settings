# Generated by Django 2.1.15 on 2020-10-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empmodel',
            fields=[
                ('SOURCE_ACCT', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'CHANNEL_BILLS_FINAL',
            },
        ),
    ]
