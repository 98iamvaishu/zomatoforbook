# Generated by Django 2.1 on 2018-11-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20181118_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
