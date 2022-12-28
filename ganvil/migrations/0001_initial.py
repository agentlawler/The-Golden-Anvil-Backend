# Generated by Django 4.1.4 on 2022-12-28 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
            ],
        ),
    ]
