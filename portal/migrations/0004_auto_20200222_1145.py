# Generated by Django 3.0.3 on 2020-02-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_remove_files_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]