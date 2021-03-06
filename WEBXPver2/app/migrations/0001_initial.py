# Generated by Django 3.0.5 on 2020-07-07 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Content Name')),
                ('type', models.CharField(choices=[('movie', 'movie'), ('show', 'show')], max_length=5, verbose_name='type')),
                ('status', models.CharField(choices=[('com', 'Fully uploaded'), ('on', 'Still uploading')], max_length=3, verbose_name='status')),
                ('studio', models.CharField(max_length=128, verbose_name='Make By')),
                ('year', models.CharField(max_length=5, verbose_name='Publish Year')),
                ('country', models.CharField(max_length=128, verbose_name='Country Make')),
                ('poster', models.FileField(default=None, upload_to='', verbose_name='poster')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=4, verbose_name='Ep Num')),
                ('name', models.CharField(max_length=128, verbose_name='Ep Name')),
                ('link', models.FileField(default=None, upload_to='', verbose_name='link')),
            ],
            options={
                'verbose_name': 'Episode',
                'verbose_name_plural': 'Episodes',
            },
        ),
        migrations.CreateModel(
            name='ErrorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='ERROR')),
                ('description', models.CharField(max_length=128, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Error',
                'verbose_name_plural': 'Errors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='HR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('birth', models.DateField(default=None, verbose_name='BirthDay')),
                ('country', models.CharField(max_length=128, verbose_name='Nationality')),
                ('JobChoices', models.CharField(choices=[('dir', 'director'), ('act', 'actor')], max_length=5, verbose_name='job')),
                ('image', models.FileField(default=None, upload_to='', verbose_name='image')),
            ],
            options={
                'verbose_name': 'HR',
                'verbose_name_plural': 'HRs',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='UserName')),
                ('email', models.CharField(max_length=128, verbose_name='Login Email')),
                ('password', models.CharField(max_length=25, verbose_name='Password')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created on')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecloset', to='app.User')),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Lists',
            },
        ),
        migrations.CreateModel(
            name='WatchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='watch time')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Episode', verbose_name='content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WatchHistory', to='app.User', verbose_name='user')),
            ],
            options={
                'verbose_name': 'history',
                'verbose_name_plural': 'histories',
            },
        ),
        migrations.CreateModel(
            name='UserListDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='app.UserList', verbose_name='list')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Detail',
                'verbose_name_plural': 'Details',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Show Name')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seasons', to='app.Content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='Reported At')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Episode', verbose_name='Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='app.User', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
        migrations.AddField(
            model_name='episode',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='app.Season', verbose_name='episode'),
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Content', verbose_name='movie/show')),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.HR', verbose_name='crew')),
            ],
            options={
                'verbose_name': 'Crew',
                'verbose_name_plural': 'Crews',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Genre', verbose_name='Genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Content', verbose_name='Movie')),
            ],
            options={
                'verbose_name': 'Classification',
                'verbose_name_plural': 'Classifications',
            },
        ),
    ]
