from contacts.models import Contact
from tasks.models import Task
from django.contrib.auth.models import User
import datetime

def contacts(user,username,lastname,color,initials):
    Contact.objects.get_or_create(
          user=user,
          name=f"{username} {lastname}",
          email=f"{username}@web.com",
          color= color,
          initials=initials       )

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

def guest_tasks(user):
    tasks(user, "Added Task erstellen", "Erstelle die komplette addedTask Seite", "urgent", "Technical Task", "Todo", datetime.date.today())
    tasks(user, "Kontakt Seite erstellen", "Erstelle die komplette Seite Kontakte", "medium", "Technical Task", "InProgress", datetime.date.today())
    tasks(user, "Board.html erstellen", "Erstelle die komplette Seite für das Board", "low", "User Story", "AwaitFeedback", datetime.date.today())
    tasks(user, "added Task auf Board erstellen", "erstelle die addTask oder passe die addtasks von der addtask HTML-Seite an", "medium", "User Story", "Done", datetime.date.today())
    tasks(user, "Log in Seite erstellen", "Erstelle die Seite zum Login", "low", "Technical Task", "Todo", datetime.date.today())