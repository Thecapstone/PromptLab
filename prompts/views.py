from django.shortcuts import render
from rest_framework import viewsets
from .models import Prompt
from .serializers import PromptSerializer
# Create your views here.

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
