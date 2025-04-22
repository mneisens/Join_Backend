from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer
from rest_framework.decorators import api_view



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def by_kanban_category(self, request):
        tasks = self.get_queryset()
        
        result = {
            'Todo': TaskSerializer(tasks.filter(kanban_category='Todo'), many=True).data,
            'InProgress': TaskSerializer(tasks.filter(kanban_category='InProgress'), many=True).data,
            'AwaitFeedback': TaskSerializer(tasks.filter(kanban_category='AwaitFeedback'), many=True).data,
            'Done': TaskSerializer(tasks.filter(kanban_category='Done'), many=True).data,
        }
        
        return Response(result)
    
    
    @action(detail=True, methods=['patch'])
    def update_category(self, request, pk=None):
        task = self.get_object()
        new_category = request.data.get('kanban_category')
        
        if new_category not in dict(Task.KANBAN_CHOICES).keys():
            return Response(
                {'error': 'Invalid kanban category'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        task.kanban_category = new_category
        task.save()
        
        return Response(TaskSerializer(task).data)



class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def tasks_by_kanban_category(request):
    tasks = Task.objects.all()
    grouped = {
        'Todo': [],
        'InProgress': [],
        'AwaitFeedback': [],
        'Done': [],
    }

    for task in tasks:
        category = task.kanban_category
        if category in grouped:
            grouped[category].append(TaskSerializer(task).data)

    return Response(grouped)