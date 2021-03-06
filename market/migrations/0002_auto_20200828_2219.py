# Generated by Django 3.1 on 2020-08-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='addr',
        ),
        migrations.AddField(
            model_name='market',
            name='adr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='bus',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='famous',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='h_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='ma',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='store_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='tel',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
