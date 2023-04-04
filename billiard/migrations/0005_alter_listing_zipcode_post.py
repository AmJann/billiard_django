# Generated by Django 4.1.7 on 2023-04-04 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billiard', '0004_news_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('body', models.TextField(max_length=6000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]