from django.db import models

class Mentor(models.Model):
    MentorID = models.CharField(max_length = 10, primary_key = True)
    MentorName = models.TextField(max_length = 20)
    RoomNo = models.IntegerField(max_length = 4)