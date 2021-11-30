from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
     list_display = ('id', 'fname', 'mname', 'lname', 'age', 'gender', 'address', 'email', 'mobno', 'alemail', 'almobno', 'fathername', 'mothername', 'insname')