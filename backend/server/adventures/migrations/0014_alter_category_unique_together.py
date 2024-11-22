# Generated by Django 5.0.8 on 2024-11-17 21:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0013_remove_adventure_type_alter_adventure_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'user_id')},
        ),
    ]
