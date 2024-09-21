from django.contrib import admin
from .models import Room, Topic, Message

class RoomDisplay(admin.ModelAdmin):
    list_display = ('host', 'name', 'description', 'topic')


class TopicDisplay(admin.ModelAdmin):
    list_display = ('id','name')


class MessageDisplay(admin.ModelAdmin):
    list_display=('user', 'room', 'body')

admin.site.register(Room,RoomDisplay)
admin.site.register(Topic, TopicDisplay)
admin.site.register(Message, MessageDisplay)
