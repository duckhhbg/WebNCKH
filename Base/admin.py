from django.contrib import admin
from .models import Ctdt, Subject, Major,User,Chapter,File,Department,Test,ChoiceQuiz,Evaluate
# Register your models here.
admin.site.register(User)
admin.site.register(Ctdt)
admin.site.register(Major)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(File)
admin.site.register(Department)
admin.site.register(Test)
admin.site.register(ChoiceQuiz)
admin.site.register(Evaluate)