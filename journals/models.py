from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Note(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}. {self.text}'

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.id}. {self.text}'

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}. {self.text}'

class JournalItem(models.Model):
    NOTE = 'N'
    TASK = 'T'
    EVENT = 'E'

    # define types of items for the item_type field
    ITEM_TYPES = (
        (NOTE, 'Note'),
        (TASK, 'Task'),
        (EVENT, 'Event'),
    )

    # item_type denotes whether the JournalItem is a Note, Task or Event object
    item_type = models.CharField(max_length=1, choices=ITEM_TYPES)

    # the user that is creating the item
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # ... other fields that will be on every Note, Task or Event

    # mandatory fields for setting up GenericRelations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="object_item")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')