from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('pk','user', 'title', 'photo')
  list_display_links=('user',)

  


