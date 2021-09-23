# Generated by Django 3.2.7 on 2021-09-22 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryCafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image1', models.ImageField(upload_to='main/')),
                ('image2', models.ImageField(upload_to='main/')),
                ('image3', models.ImageField(upload_to='main/')),
                ('content', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallerycafe', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
