from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    team = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.JSONField(default=list)

class Activity(models.Model):
    user = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

class Workout(models.Model):
    user = models.CharField(max_length=150)
    workout_type = models.CharField(max_length=100)
    details = models.TextField()
    suggested_by = models.CharField(max_length=150, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
