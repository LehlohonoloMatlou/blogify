from django.contrib import admin

from .models import Audience
from .models import Article
# Register your models here.

admin.site.register(Audience)
admin.site.register(Article)