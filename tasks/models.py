from django.db import models
from contacts.models import Contact
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    CATEGORY_CHOICES = [
        ('Technical Task', 'Technical Task'),
        ('User Story', 'User Story'),
    ]
    
    KANBAN_CHOICES = [
        ('Todo', 'To Do'),
        ('InProgress', 'In Progress'),
        ('AwaitFeedback', 'Await Feedback'),
        ('Done', 'Done'),
    ]

    kanban_category = models.CharField(
        max_length=15, 
        choices=KANBAN_CHOICES,
        default='Todo'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    header = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    kanban_category = models.CharField(max_length=50, choices=KANBAN_CHOICES, default='Todo')
    assigned_to = models.ManyToManyField(Contact, related_name='tasks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.header

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    subtask = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.subtask