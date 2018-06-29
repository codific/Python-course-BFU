from django.db import models

# Create your models here.


class Poll(models.Model):

    question = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        unique_together = ['question', 'pub_date']

    def __str__(self):
        return self.question


class Choice(models.Model):

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.PositiveIntegerField(default=0)
    # Self relation
    # null - auto insert null when new record is added
    # blank - allow blank fields in forms
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    # Auto timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice_text