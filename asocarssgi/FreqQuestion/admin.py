#-*- coding: utf-8 -*-
from django.contrib import admin
from FreqQuestion.models import Topic, Questions, Answer 

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['qutopic', 'questio', 'pubdate']
    fieldsets = (
        (u'Pregunta', {
            'fields': ('qutopic', 'questio', 'pubdate',)
        }),
        (u'Datos de diligenciamiento',{
            'fields': ('whopost', 'whoposi', 'whocorp')
        }),
    )

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['questio', 'answers', 'aproved'] 
    fieldsets = (
        (u'Respuesta', {
            'fields': ('questio', 'answers')
        }),
        (u'Datos de diligenciamiento',{
            'fields': ('whoansr', 'sources', 'whoposi', 'whocorp')
        }),
        (u'Aprobación',{
            'fields': ('aproved', 'whoapro', 'datapro')
        }),
    )
admin.site.register(Topic)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
