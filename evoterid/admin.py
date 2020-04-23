from django.contrib import admin
from .models import User
from .models import Suggestion
from .models import modification

admin.site.register(User)
admin.site.register(modification)
admin.site.register(Suggestion)
# Register your models here.
