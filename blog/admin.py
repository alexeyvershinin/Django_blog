from django.contrib import admin
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    # поле slug автоматически предзаполняется при наборе заголовка на клавиатуре
    prepopulated_fields = {'slug': ('title',)}
    # поисковой виджет для отбора ассоциированных объектов для поля author
    raw_id_fields = ['author']
    # навигационные ссылки для навигации по иерархии дат
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'moderated']
    list_filter = ['moderated', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
