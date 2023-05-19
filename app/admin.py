from django.contrib import admin
from .models import *

class ScoreFilter(admin.SimpleListFilter):
    title = 'Score Filter'
    parameter_name = 'score'

    def lookups(self, request, model_admin):
        return (
            ("0-9", '0-9'),
            ("10-19", '10-19'),
            ("20-29", '20-29'),
            ("30<=", '30 and above'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-9':
            return queryset.filter(score__lte=9)
        if self.value() == '10-19':
            return queryset.filter(score__range=(10, 19))
        if self.value() == '20-29':
            return queryset.filter(score__range=(20, 29))
        if self.value() == '30<=':
            return queryset.filter(score__gte=30)

# Register your models here.
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
    list_filter = (ScoreFilter,)
    search_fields = ['user__email', 'user__username']
#admin.site.register(Score, ScoreFilter)