from django.db import models
from django.conf import settings

class Task(model.Model):
    class Priority(Models.TexChoices):
        BAIXA = ""
        MEDIA =
        ALTA =