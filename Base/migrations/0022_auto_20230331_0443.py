# Generated by Django 3.2.7 on 2023-03-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0021_alter_evaluate_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluate',
            name='evaluate',
            field=models.CharField(choices=[('Đ', 'Đ'), ('CĐ', 'CĐ')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='choicequiz',
            name='ans',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default=0, max_length=1),
        ),
    ]
