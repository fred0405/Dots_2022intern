# Generated by Django 4.0.2 on 2022-02-28 04:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.TextField(default='')),
                ('xp', models.IntegerField(default=0)),
                ('gold', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'player',
            },
        ),
    ]
