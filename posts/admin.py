from django.contrib import admin

from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","lead","updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
