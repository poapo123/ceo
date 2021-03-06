# Generated by Django 2.2 on 2020-06-20 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceo', '0003_auto_20200620_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodstuff',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='fsstorage',
            name='recipe',
        ),
        migrations.AddField(
            model_name='fsstorage',
            name='foodstuff',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ceo.Foodstuff'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='fsstorage',
            name='fss_img_file_path',
            field=models.ImageField(blank=True, null=True, upload_to='fs_storage/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='document_file_path',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_img_file_path',
            field=models.ImageField(blank=True, null=True, upload_to='recipe/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='upload_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video_file_path',
            field=models.FileField(upload_to='video/'),
        ),
        migrations.CreateModel(
            name='RFRealatoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodstuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceo.Foodstuff')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceo.Recipe')),
            ],
        ),
    ]
