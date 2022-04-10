from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id','title','url')
