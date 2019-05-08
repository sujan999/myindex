# Generated by Django 2.2 on 2019-05-06 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='story/')),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=True)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Tag')),
            ],
            options={
                'verbose_name': 'My Story',
                'verbose_name_plural': 'My Stories',
                'ordering': ['-date'],
            },
        ),
    ]
