from django.contrib import admin

# Register your models here.
from .models import Post
# el "." serveix per indicar que busqui el "models" on estàs

admin.site.register(Post)
