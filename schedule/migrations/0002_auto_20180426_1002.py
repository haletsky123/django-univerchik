# Generated by Django 2.0.4 on 2018-04-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='name',
            field=models.CharField(max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='ecpec',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]