# Generated by Django 4.2.17 on 2024-12-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsserTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nickname', models.CharField(default='', max_length=100)),
                ('user_task', models.CharField(default='', max_length=255)),
            ],
        ),
    ]