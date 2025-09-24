from django.db import models
from users_app.models import Profile

class Trip(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    posts = models.ManyToManyField('blog_app.Post', blank=True)

    def __str__(self):
        return self.name
