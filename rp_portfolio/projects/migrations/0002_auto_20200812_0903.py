# Generated by Django 2.2.10 on 2020-08-12 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
