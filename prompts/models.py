from django.db import models
from django.contrib.auth.models import User
import uuid

class Prompt(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='prompts',
        default=1,
    )
    prompt =models.TextField() #Field that will contain the Prompt
    tags = models.CharField(max_length=200) # Field that will contain the Tags
    expected_output = models.ImageField(upload_to='media/prompts/expected_output/', blank=True, null=True) # Field that will contain the Expected Output Image