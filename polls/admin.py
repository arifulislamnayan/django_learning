from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
	model= Choice
	extra=2



class QuestionAdmin(admin.ModelAdmin):
	#fields=['question_text','pub_date']
	fieldsets = [
		('Questions', {'fields':['question_text'],'classes':['collapse']}),

		('Date Information', {'fields':['pub_date'],'classes':['collapse']})




	]
	list_display = ('question_text', 'pub_date','was_published_recently')
	inlines = [ChoiceInline]
	list_filter =['pub_date']
	search_fields =['question_text']
	



admin.site.register(Question, QuestionAdmin)


admin.site.register(Choice)



# Register your models here.
