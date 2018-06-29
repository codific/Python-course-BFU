from django.db import models

# Create your models here.


class Poll(models.Model):

    question = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question


class Choice(models.Model):

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.choice_text