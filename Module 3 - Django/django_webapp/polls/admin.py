from django.contrib import admin
from .models import Poll, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):

    # We can have either fields or fieldsets, but not both at the same time
    # fields = ('question', 'pub_date')
    search_fields = ['question']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'

    fieldsets = [
        (None, {'fields': ['question']}),
        ('Publication date', {'fields': ['pub_date'],
                              'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_per_page = 2

    # Making fields readonly
    def get_readonly_fields(self, request, obj=None):
        return ('pub_date', )


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)