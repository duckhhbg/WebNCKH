# Generated by Django 3.2.7 on 2023-03-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0015_auto_20230324_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='ctdt',
            name='SoTc',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=0, max_length=1),
        ),
    ]