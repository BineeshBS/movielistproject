# Generated by Django 4.1.6 on 2023-02-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='jljljjlj', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
