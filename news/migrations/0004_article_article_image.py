# Generated by Django 3.2.9 on 2021-11-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20211124_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]