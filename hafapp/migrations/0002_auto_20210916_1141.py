# Generated by Django 3.2.6 on 2021-09-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hafapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='friends',
            field=models.ManyToManyField(related_name='orders', to='hafapp.Friend'),
        ),
    ]