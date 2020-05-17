from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    post_id=models.AutoField(primary_key= True)
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    content=models.TextField()
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.title+" by "+ self.author
