# Generated by Django 2.0.6 on 2018-09-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='html_content',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]