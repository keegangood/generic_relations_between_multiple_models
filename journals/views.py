from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JournalItemSerializer
from journals.models import Note, Task, Event, JournalItem

@api_view(['GET'])
def get_journal_items(request):
    # delete all JournalItems, Notes and Tasks for testing
    JournalItem.objects.all().delete()
    Note.objects.all().delete()
    Task.objects.all().delete()
    Event.objects.all().delete()

    # This will ultimately be request.user
    user = get_user_model().objects.first()


    # create an event, notes, and tasks
    event_1 = Event.objects.create(title=f"Event {Event.objects.count() + 1}") # 1. Event 1
    
    task_1 = Task.objects.create(title=f"Task {Task.objects.count() + 1}") # 1. Task 1
    task_2 = Task.objects.create(title=f"Task {Task.objects.count() + 1}") # 2. Task 2
    
    note_1 = Note.objects.create(title=f"Note {Note.objects.count() + 1}") # 1. Note 1
    note_2 = Note.objects.create(title=f"Note {Note.objects.count() + 1}") # 2. Note 2
    

    # create JournalItem objects to store the new event, tasks and notes
    j_event_1 = JournalItem.objects.create(content_object=event_1, item_type='E', owner=user)
    
    j_task_1 = JournalItem.objects.create(content_object=task_1, item_type='T', owner=user)
    j_task_2 = JournalItem.objects.create(content_object=task_2, item_type='T', owner=user)
    
    j_note_1 = JournalItem.objects.create(content_object=note_1, item_type='N', owner=user)
    j_note_2 = JournalItem.objects.create(content_object=note_2, item_type='N', owner=user)


    print(j_event_1)
    print(j_task_1)
    print(j_task_2)
    print(j_note_1)
    print(j_note_2)