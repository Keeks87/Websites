from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):

    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
