from django.contrib import admin
from home.models import Home
from home.models import User
from home.models import BookingHistory
# Register your models here.

admin.site.register(Home)
admin.site.register(User)
admin.site.register(BookingHistory)
