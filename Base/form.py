from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email']

class CtdtForm(ModelForm):
    class Meta:
        model = Ctdt
        fields = ['name']

class MajorForm(ModelForm):
    class Meta:
        model = Major
        fields = ['name']

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        exclude = ['host','participants']

class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
        exclude = ['fksubject']

class DepartmentrForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['fkchapter','file']
        exclude = ['fkchapter']

class EvaluateForm(ModelForm):
    class Meta:
        model = Evaluate
        fields = '__all__'

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionForm(ModelForm):
    class Meta:
        model = ChoiceQuiz
        fields = '__all__'