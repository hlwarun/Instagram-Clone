# Generated by Django 3.1.2 on 2020-10-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment_body',
            field=models.CharField(default='Hello', max_length=200),
        ),
    ]