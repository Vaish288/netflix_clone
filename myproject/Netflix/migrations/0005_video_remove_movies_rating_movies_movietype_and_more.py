# Generated by Django 5.0.4 on 2024-04-24 07:28

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix', '0004_remove_description_cast_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='videos')),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='rating',
        ),
        migrations.AddField(
            model_name='movies',
            name='movietype',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('seasons', 'Seasons')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='thumbnailImage',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail'),
        ),
        migrations.AddField(
            model_name='movies',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='movietype',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('seasons', 'Seasons')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='thumbnailImage',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail'),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='tvshows',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('mobile_no', models.CharField(max_length=12, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('subscription_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profiles', to='Netflix.subscriptionplan')),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='video',
            field=models.ManyToManyField(to='Netflix.video'),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='video',
            field=models.ManyToManyField(to='Netflix.video'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('profiles', models.ManyToManyField(blank=True, null=True, to='Netflix.profile')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]