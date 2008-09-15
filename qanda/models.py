from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=32)
    create_date = models.DateTimeField('date created')
    times_viewed = models.IntegerField()

class RelatedTag(models.Model):
    start_tag = models.ForeignKey(Tag, related_name='start_tag')
    related_tag = models.ForeignKey(Tag, related_name='related_tag')
    times_together = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    display_name = models.CharField(max_length=64)
    create_date = models.DateTimeField('signup date')
    email = models.EmailField()

class Question(models.Model):
    question = models.CharField(max_length=255)
    ask_date = models.DateTimeField('date asked')
    times_viewed = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=255)
    answer_date = models.DateTimeField('date answered')
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User)
    rating = models.IntegerField()
