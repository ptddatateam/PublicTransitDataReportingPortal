# Generated by Django 2.2.5 on 2019-09-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Panacea', '0022_auto_20190920_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover_sheet',
            name='service_website_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]