# Generated by Django 3.2.7 on 2023-03-19 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fksubject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.subject')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='Avatars/avatar.svg', null=True, upload_to='Avatars/'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='Documents/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fkchapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.chapter')),
            ],
        ),
    ]
