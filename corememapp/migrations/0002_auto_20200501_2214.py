# Generated by Django 3.0.5 on 2020-05-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corememapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='bodytext',
            field=models.TextField(blank=True, null=True, verbose_name='Memory Content'),
        ),
    ]
