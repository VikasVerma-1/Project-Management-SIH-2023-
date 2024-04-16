# Generated by Django 3.1.14 on 2024-04-16 14:27

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(blank=True, max_length=50, null=True)),
                ('college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('university_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_demo_user', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]