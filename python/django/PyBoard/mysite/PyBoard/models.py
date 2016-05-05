from django.db import models

# Create your models here.
class Topic(models.Model):
    """ Topic Table """
    title = models.CharField(max_length=500)
    register_name = models.CharField(max_length=20)
    register_datetime = models.DateTimeField()
    update_name = models.CharField(max_length=20)
    update_datetime = models.DateTimeField()

    def __str__(self):
        return self.title

class TopicDetail(models.Model):
    """ TopicDetail Table """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    register_name = models.CharField(max_length=20)
    register_datetime = models.DateTimeField()
    update_name = models.CharField(max_length=20)
    update_datetime = models.DateTimeField()

