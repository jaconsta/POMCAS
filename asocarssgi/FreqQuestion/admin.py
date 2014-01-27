#-*- coding: utf-8 -*-
from django.contrib import admin
from FreqQuestion.models import Topic, Questions, Answer 

admin.site.register(Topic)
admin.site.register(Questions)
admin.site.register(Answer)
