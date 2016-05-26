from django.db import models

# Create your models here.
class Topic(models.Model):
    """ Topic Table """
    title = models.CharField(max_length=500)
    register_name = models.CharField(max_length=30)
    register_datetime = models.DateTimeField()
    update_name = models.CharField(max_length=30)
    update_datetime = models.DateTimeField()

    def __str__(self):
        return self.title

class TopicDetail(models.Model):
    """ TopicDetail Table """
    title = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    text_no = models.PositiveIntegerField(blank=False, null=False, default=1)
    register_name = models.CharField(max_length=30)
    register_datetime = models.DateTimeField()
    update_name = models.CharField(max_length=30)
    update_datetime = models.DateTimeField()
