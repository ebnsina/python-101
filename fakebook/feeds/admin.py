from django.contrib import admin
from .models import Feed, Comment


class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feed, FeedAdmin)
admin.site.register(Comment, CommentAdmin)
