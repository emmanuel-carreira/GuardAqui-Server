# Generated by Django 2.1.3 on 2018-11-08 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0021_auto_20181108_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='dataHora',
            new_name='datahora',
        ),
    ]
