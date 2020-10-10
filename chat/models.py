from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Participants(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.user.first_name

    @property
    def room(self):
        return self.rooms_set.all()
        
class Rooms(models.Model):
    
    # Room title
    title = models.CharField(max_length=255)
    admin = models.CharField(max_length=255,default=" ")
    group_members = models.ManyToManyField(User)

    # If only "staff" users are allowed (is_staff on django's User)
    # staff_only = models.BooleanField(default=False)


    def __str__(self):
        return self.title

# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#    gender = models.BooleanField(default=True) # True for male and False for female
#    # you can add more fields here.
    

class friendsCount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends_count = models.IntegerField(default=1)

class Message(models.Model):
    author = models.ForeignKey(User, related_name='messages', on_delete=models.PROTECT)
    group_name = models.CharField(max_length=256,null=False,blank=False,default='family')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last20_messages(room_name_chat):
        # q = Message.objects.filter(group_name = room_name_chat)
        # print(q)
        q = Message.objects.order_by('-timestamp').filter(group_name=room_name_chat)[:20]
        print(f'q =========== {q}')
        return q