from django.contrib import admin
from .models import Message, Thread

# Register your models here.
class MessengerAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')


admin.site.register(Message, MessengerAdmin)
admin.site.register(Thread)