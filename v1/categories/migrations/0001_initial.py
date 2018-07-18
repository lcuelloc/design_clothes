# Generated by Django 2.0.6 on 2018-07-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='updated')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-id'],
                'get_latest_by': 'created',
            },
        ),
    ]
