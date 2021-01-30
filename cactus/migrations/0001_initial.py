# Generated by Django 3.1.5 on 2021-01-30 05:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_file', models.ImageField(unique=True, upload_to='pictures')),
                ('picture_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CactusModel',
            fields=[
                ('cactus_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cactus_name', models.CharField(max_length=50)),
                ('cactus_scientific_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cactus_description', models.TextField(blank=True, max_length=200, null=True)),
                ('cactus_size', models.CharField(choices=[('S', 'Pequeño'), ('M', 'Mediano'), ('L', 'Grande')], max_length=1)),
                ('cactus_picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cactus.picturemodel')),
            ],
            options={
                'db_table': 'cactus',
            },
        ),
    ]