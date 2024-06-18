from django.contrib import admin

from .models import Category, Course

EMPTY = '-пусто-'

admin.site.site_header = 'Админка магазина курсов'
admin.sites.site_title = 'Курсы'
admin.sites.index_title = 'Добро пожаловать'


class CoursesInline(admin.TabularInline):
    model = Course
    extra = 0
    exclude = ('created_at',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('pk', 'title',)
    search_fields = ('title',)
    readonly_fields = ('id',)
    list_filter = ('created_at',)
    fieldsets = (
        (None, {'fields': ('id', 'title',)}),
        ('Dates', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    inlines = (CoursesInline,)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'students_qty',
                    'comments_qty', 'created_at',)
    list_display_links = ('id', 'title',)
    readonly_fields = ('id',)
    search_fields = ('title',)
    list_filter = ('created_at', 'price',)
    empty_value_display = '-EMPTY-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
