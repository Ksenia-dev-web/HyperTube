# Generated by Django 2.2 on 2022-03-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_auto_20220312_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
