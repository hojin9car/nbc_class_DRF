# Generated by Django 4.0.5 on 2022-06-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, verbose_name='비밀번호'),
        ),
    ]