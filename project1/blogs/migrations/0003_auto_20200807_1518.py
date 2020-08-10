# Generated by Django 2.2.10 on 2020-08-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('content', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
