# Generated by Django 3.1.4 on 2022-04-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
    ]