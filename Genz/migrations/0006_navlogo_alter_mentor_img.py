# Generated by Django 5.1.2 on 2024-11-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genz', '0005_mentor_socialmediaprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='navLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='logo/')),
            ],
        ),
        migrations.AlterField(
            model_name='mentor',
            name='img',
            field=models.ImageField(upload_to='mentors/'),
        ),
    ]
