# Generated by Django 3.0.3 on 2020-06-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceo', '0007_recipe_recipe_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fsstorage',
            name='fss_img_file_path',
            field=models.ImageField(blank=True, null=True, upload_to='fs_storage/img/'),
        ),
    ]
