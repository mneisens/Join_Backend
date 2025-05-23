# Generated by Django 5.2 on 2025-04-13 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0002_rename_first_name_contact_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateField()),
                ('priority', models.CharField(choices=[('urgent', 'Urgent'), ('medium', 'Medium'), ('low', 'Low')], default='low', max_length=20)),
                ('category', models.CharField(choices=[('Technical Task', 'Technical Task'), ('User Story', 'User Story')], max_length=50)),
                ('kanban_category', models.CharField(choices=[('Todo', 'Todo'), ('In Progress', 'In Progress'), ('Awaiting Feedback', 'Awaiting Feedback'), ('Done', 'Done')], default='Todo', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ManyToManyField(blank=True, related_name='tasks', to='contacts.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='tasks.task')),
            ],
        ),
    ]
