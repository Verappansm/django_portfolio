from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)  # Comma-separated tech stack
    github_link = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Patent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    google_link = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    google_link = models.URLField(max_length=500)

    def __str__(self):
        return self.title

