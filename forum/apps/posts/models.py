from django.db import models
from django.utils.timezone import now
from accounts.models import UserAccount 


class Post(models.Model):
    class Category(models.TextChoices):
        SCIENCE = 'Science'
        PROGG = 'Programming'
        FILMS = 'Films'
        GAMES = 'Games'
        FOOD = 'Food'
        RELATIONS = 'Relations'

    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE, to_field='email', related_name='posts_by_author')
    pub_date = models.DateTimeField(default=now, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=Category.choices)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_to_post')
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='comments_by_author', to_field='email')
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=now, blank=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    
    def __str__(self):
        return self.text[0:13] + '...'
