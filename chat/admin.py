from django.contrib import admin

# Register your models here.
from .models import Participants,Rooms,Message

class display(admin.ModelAdmin):
    list_display = ['title','admin']

admin.site.register(Participants)
admin.site.register(Rooms,display)
admin.site.register(Message)
# admin.site.register(User)