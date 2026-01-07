from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'author', 'prompt', 'tags', 'expected_output']