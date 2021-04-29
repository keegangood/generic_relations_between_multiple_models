from rest_framework import serializers

from .models import JournalItem

class JournalItemSerializer(serializers.ModelSerializer):
    model = JournalItem

    fields = '__all__'