from contacts.models import Contact
from tasks.models import Task
from django.contrib.auth.models import User
import datetime
from django.db import IntegrityError
import uuid

def contacts(user, username, lastname, color, initials):
    user_id = user.username.split('_')[-1] if '_' in user.username else str(uuid.uuid4())[:3]
    base_email = f"{username.lower()}@web.com"
    try:
        contact, created = Contact.objects.get_or_create(
            user=user,
            name=f"{username} {lastname}",
            email=base_email,
            defaults={
                'color': color,
                'initials': initials
            }
        )
        if created:
            return contact
    except IntegrityError:
        pass
    
    unique_id = str(uuid.uuid4())[:3]
    contact = Contact.objects.create(
        user=user,
        name=f"{username} {lastname}",
        email=f"{username.lower()}_{unique_id}@web.com",
        color=color,
        initials=initials
    )
    return contact

def tasks(user,headher,description,pritority,category,kanban_category,due_date):
    Task.objects.get_or_create(
        user=user,
        header=headher,
        description=description,
        priority=pritority,
        category=category,
        kanban_category=kanban_category,
        due_date=due_date,
    )


def guest_contact(user):
    try:
        contacts(user,"Peter", "Müller","red","PM")
        contacts(user,"Hans", "Mayer","green","HM")
        contacts(user,"Klaus", "Schmidt","blue","KS")   
        contacts(user,"Michael", "Schmidt","blue", "MS")
        contacts(user,"Anna", "Schneider","green","AS")
        contacts(user,"Laura", "Fischer","purple","LF")
        contacts(user,"Markus", "Weber","orange","MW")
        contacts(user,"Julia", "Hoffmann","pink","JH")
        contacts(user,"Sandra", "Winter","brown","SW")
        contacts(user,"Tobias", "Schneider","gray","TS")
    except IntegrityError:
        pass

def guest_tasks(user):
    tasks(user, "Added Task erstellen", "Erstelle die komplette addedTask Seite", "urgent", "Technical Task", "Todo", datetime.date.today())
    tasks(user, "Kontakt Seite erstellen", "Erstelle die komplette Seite Kontakte", "medium", "Technical Task", "InProgress", datetime.date.today())
    tasks(user, "Board.html erstellen", "Erstelle die komplette Seite für das Board", "low", "User Story", "AwaitFeedback", datetime.date.today())
    tasks(user, "added Task auf Board erstellen", "erstelle die addTask oder passe die addtasks von der addtask HTML-Seite an", "medium", "User Story", "Done", datetime.date.today())
    tasks(user, "Log in Seite erstellen", "Erstelle die Seite zum Login", "low", "Technical Task", "Todo", datetime.date.today())