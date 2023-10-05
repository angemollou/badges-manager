# Generated by Django 4.2.5 on 2023-10-04 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to='badge.mybadgeuser', verbose_name='Assignee'),
        ),
        migrations.AddField(
            model_name='task',
            name='responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_tasks', to='badge.mybadgeuser', verbose_name='Responsible'),
        ),
    ]