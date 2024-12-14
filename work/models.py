# work/models.py
from django.db import models

class WorkExperience(models.Model):
    INTERNSHIP = 'Internship'
    RESPONSIBILITY = 'Position of Responsibility'

    EXPERIENCE_CHOICES = [
        (INTERNSHIP, 'Internship'),
        (RESPONSIBILITY, 'Position of Responsibility'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Optional if currently ongoing
    experience_type = models.CharField(
        max_length=50,
        choices=EXPERIENCE_CHOICES,
        default=INTERNSHIP
    )

    def __str__(self):
        return self.title
