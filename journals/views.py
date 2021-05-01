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


    # create a task, two notes and an event
    task_1 = Task.objects.create(title="Walk the dog")
    
    note_1 = Note.objects.create(title="Avoid Main St.")
    note_2 = Note.objects.create(title="Bring flashlight")
    
    event_1 = Event.objects.create(title="Saw a raccoon!")

    # create JournalItem objects to store the new event, tasks and notes
    j_task_1 = JournalItem.objects.create(content_object=task_1, item_type='T', owner=user)
    
    j_note_1 = JournalItem.objects.create(content_object=note_1, item_type='N', owner=user)
    j_note_2 = JournalItem.objects.create(content_object=note_2, item_type='N', owner=user)

    j_event_1 = JournalItem.objects.create(content_object=event_1, item_type='E', owner=user)

    print(j_task_1)
    print(j_note_1)
    print(j_note_2)
    print(j_event_1)

    print(j_task_1.content_object)
    print(j_note_1.content_object)