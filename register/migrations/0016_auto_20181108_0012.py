# Generated by Django 2.1.3 on 2018-11-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_auto_20181108_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='null@null.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
