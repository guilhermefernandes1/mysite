from django.contrib import admin

from .models import Question, Choice


#class QuestionAdmin(admin.ModelAdmin):
#	fields = ['pub_date', 'question_text']


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3   # How many choices' field by default


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Question',	{'fields': ['question_text'], 'classes': ['colapse']}),
		('Date Information',	{'fields': ['pub_date'], 'classes': ['colapse']}),
	]
	inlines = [ChoiceInline]
	
	list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

