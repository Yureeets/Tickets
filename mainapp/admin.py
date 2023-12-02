from django.contrib import admin
from .models import Ticket, Passenger, Flight

admin.site.register(Ticket)
admin.site.register(Passenger)
admin.site.register(Flight)
