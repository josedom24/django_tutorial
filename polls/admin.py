from django.contrib import admin

<<<<<<< HEAD
from .models import Choice, Question, Categoria
=======
from .models import Choice, Question
>>>>>>> bc6295723152e1e860cfa52200c992f903c3e498


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
<<<<<<< HEAD
admin.site.register(Categoria)
=======
>>>>>>> bc6295723152e1e860cfa52200c992f903c3e498
