# Generated by Django 3.2.6 on 2021-08-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
