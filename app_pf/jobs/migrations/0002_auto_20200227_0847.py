# Generated by Django 2.0.2 on 2020-02-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='ENTER TITLE', max_length=50),
        ),
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.TextField(default='ENTER URL'),
        ),
    ]