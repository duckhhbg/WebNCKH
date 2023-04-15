# Generated by Django 3.2.7 on 2023-03-22 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_subject_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='fkctdt',
        ),
        migrations.AddField(
            model_name='subject',
            name='fkmajor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.major'),
        ),
    ]