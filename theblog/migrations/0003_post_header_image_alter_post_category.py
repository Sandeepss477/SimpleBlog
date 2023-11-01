# Generated by Django 4.2.6 on 2023-10-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]