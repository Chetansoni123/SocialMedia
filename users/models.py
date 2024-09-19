from django.db import models
from django.contrib.auth.models import User
from PIL import Image 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')

    def __str__(self):
        return f'{self.user.username} Profile'



class Mobile(models.Model):
    user_mobile = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.mobile



class friends(models.Model):
    conn_user = models.CharField(max_length=50)
    user_friend = models.ManyToManyField(User)

    def __str__(self):
        return self.conn_user


class countFriends(models.Model):
    count = models.IntegerField(unique=False)
    user_count = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.count