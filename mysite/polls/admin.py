from django.contrib import admin
from .models import Question
# Register your models here.
 


class QuestionAdmin(admin.ModelAdmin):
    fieldsets=("Question",{"fields":('question_text', 'pub_date')}),


admin.site.register(Question,QuestionAdmin)