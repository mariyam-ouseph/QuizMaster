from django.contrib import admin

# Register your models here.
from trivia.models import User, Subject

admin.site.register(User)

admin.site.register(Subject)

