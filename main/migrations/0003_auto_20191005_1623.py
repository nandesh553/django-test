# Generated by Django 2.2.5 on 2019-10-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191005_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, default='', help_text='Company Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.CharField(blank=True, help_text='Company Type', max_length=250),
        ),
    ]
