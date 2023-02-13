# Generated by Django 3.2.17 on 2023-02-05 15:29

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('style', models.CharField(blank=True, choices=[
                    ('Traditional', 'Traditional'),
                    ('Neo-Traditional', 'Neo-Traditional'),
                    ('Japanese', 'Japanese'),
                    ('Realism', 'Realism'),
                    ('Fineline', 'Fineline'),
                    ('Blackwork', 'Blackwork'),
                    ('Color', 'Color'),
                    ('Script', 'Script'),
                    ('Other', 'Other')
                ], max_length=50)),
                ('artist', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
