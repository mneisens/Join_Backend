from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from contacts.models import Contact
from tasks.models import Task
import uuid
import datetime
from .functions import guest_contact, guest_tasks

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    u = request.data.get('username')
    p = request.data.get('password')
    if not (u and p):
        return Response({'error': 'Username und Passwort erforderlich'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=u).exists():
        return Response({'error': 'Benutzer existiert bereits'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=u, password=p)
    token, _ = Token.objects.get_or_create(user=user)
    create_user_contact(user)
    
    return Response({'token': token.key}, status=status.HTTP_201_CREATED)

def create_user_contact(user):
    import random    
    colors = ["red", "green", "blue", "purple", "orange", "pink", "brown", "gray"]
    color = random.choice(colors)
    username = user.username
    if '@' in username:
        username = username.split('@')[0]
    
    initials = username[0].upper()
    if len(username) > 1:
        initials += username[1].upper()
    
    email = user.username if '@' in user.username else f"{username}@example.com"
    
    try:
        from contacts.models import Contact
        Contact.objects.create(
            user=user,
            name=username,  
            email=email,
            color=color,
            initials=initials
        )
    except Exception as e:
        print(f"Fehler beim Erstellen des Kontakts: {e}")

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    u = request.data.get('username')
    p = request.data.get('password')

    if not u or not p:
        return Response({'error': 'Username oder Passwort fehlt'}, status=400)

    print(f"[LOGIN] Versuche Login mit: {u} / {p}")

    if not User.objects.filter(username=u).exists():
        return Response({'error': 'Benutzer existiert nicht'}, status=404)

    user = authenticate(username=u, password=p)
    if not user:
        return Response({'error': 'Passwort falsch'}, status=401)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({
            'token': token.key,
            'username': user.username,
        })



@api_view(['POST'])
@permission_classes([AllowAny])
def guest_login(request):
    username = f"guest_{uuid.uuid4().hex[:8]}"
    user = User.objects.create_user(username=username)

    token, _ = Token.objects.get_or_create(user=user)
    guest_tasks(user)
    guest_contact(user)

    return Response({'token': token.key}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    user = request.user
    Token.objects.filter(user=user).delete()
    if user.username.startswith('guest_'):
        user.delete()
    return Response(status=204)



def contacts(user,username,lastname,color,initials):
    Contact.objects.create(
          user=user,
          name=f"{username} {lastname}",
          email=f"{username}@web.com",
          color= color,
          initials=initials       )

def tasks(user,headher,description,pritority,category,kanban_category,due_date):
    Task.objects.create(
        user=user,
        header=headher,
        description=description,
        priority=pritority,
        category=category,
        kanban_category=kanban_category,
        due_date=due_date,
    )

