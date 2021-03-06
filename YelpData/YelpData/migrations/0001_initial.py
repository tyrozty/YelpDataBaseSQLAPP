# Generated by Django 2.1.3 on 2018-12-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('business_id', models.AutoField(primary_key=True, serialize=False)),
                ('business_identifier', models.CharField(max_length=255)),
                ('business_name', models.CharField(max_length=255, unique=True)),
                ('stars', models.CharField(max_length=3)),
                ('review_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'business',
                'verbose_name_plural': 'businesses',
                'db_table': 'business',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_identifier', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=11)),
                ('longitude', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_identifier', models.CharField(max_length=1024)),
                ('caption', models.CharField(max_length=1024)),
                ('label', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'db_table': 'photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_identifier', models.CharField(max_length=255)),
                ('stars', models.IntegerField()),
                ('text', models.CharField(max_length=10000)),
                ('useful', models.IntegerField()),
                ('funny', models.IntegerField()),
                ('cool', models.IntegerField()),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('tip_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=1024)),
                ('date', models.CharField(max_length=100)),
                ('likes', models.IntegerField()),
            ],
            options={
                'verbose_name': 'tip',
                'verbose_name_plural': 'tips',
                'db_table': 'tip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_identifier', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('review_count', models.IntegerField()),
                ('yelping_since', models.CharField(max_length=256)),
                ('fans', models.IntegerField()),
                ('average_stars', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
