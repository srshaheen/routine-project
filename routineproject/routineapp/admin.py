from django.contrib import admin

from .models import Course, Routine, Teacher

# Register your models here.
admin.site.register(Teacher)


class RoutineAdmin(admin.ModelAdmin):
    list_display = ('date', 't_name', 'course_name',
                    'time')
    list_filter = ('date',)
    search_fields = ('course_name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'total_class',
                    'course_credit', 't_name')
    list_filter = ('course_id',)
    search_fields = ('course_name',)


admin.site.register(Routine, RoutineAdmin)
admin.site.register(Course, CourseAdmin)
