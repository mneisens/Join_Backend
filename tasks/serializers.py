from rest_framework import serializers
from .models import Task, Subtask, Contact
from contacts.serializers import ContactSerializer

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'subtask', 'done']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    assigned_to = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Contact.objects.all(), required=False
    )
    
    class Meta:
        model = Task
        fields = ['id', 'header', 'description', 'due_date', 'priority', 
                  'category', 'kanban_category', 'assigned_to', 'subtasks', 'created_at']
    
    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_to_data = validated_data.pop('assigned_to', [])
        
        task = Task.objects.create(**validated_data)
        
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
            
        task.assigned_to.set(assigned_to_data)
        
        return task
    
    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', None)
        assigned_to_data = validated_data.pop('assigned_to', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if subtasks_data is not None:
            instance.subtasks.all().delete()
            for subtask_data in subtasks_data:
                Subtask.objects.create(task=instance, **subtask_data)
        
        if assigned_to_data is not None:
            instance.assigned_to.set(assigned_to_data)
            
        return instance