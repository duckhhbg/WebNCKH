from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# acc admin adminduc mk duc@1234

class User(AbstractUser):
    student = 'SV'
    teacher = 'GV'
    admin = 'AD'
    modelaccess = [(student,'SV'),(teacher,'GV'),(admin,'AD')]
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    access = models.CharField(choices=modelaccess,default=student,max_length=2)
    avatar = models.ImageField(upload_to='Avatars/',null=True, default="Avatars/avatar.svg")

    def is_access(self):
        return self.access in {self.student, self.teacher, self.admin}

    def __str__(self):
        return f"{self.username}"

class Major(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Ctdt(models.Model):
    fkdepartment = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    fkmajor = models.ForeignKey(Major,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    Tc = (('0','0'),('1','1'),('2','2'),('3','3'),('4','4'))
    SoTc = models.CharField(choices=Tc,default=0,max_length=1)
    modelaccess = (('0','Cơ bản'),('1','Cơ sở'),('2','Chuyên ngành'))
    access = models.CharField(choices=modelaccess,default='0',max_length=1)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    fkctdt = models.ForeignKey(Ctdt,on_delete=models.SET_NULL,null=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    numsub = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    
class Chapter(models.Model):
    fksubject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

    
class File(models.Model):
    
    fkchapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL,null=True)
    file = models.FileField(upload_to='Documents/',null=True,default=None,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

class Test(models.Model):
    fksubject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    
class ChoiceQuiz(models.Model):
    fktest = models.ForeignKey(Test, on_delete=models.SET_NULL,null=True)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    listans = (('A','A'),('B','B'),('C','C'),('D','D'))
    ans = models.CharField(choices=listans,default='A',max_length=1)
    
    def __str__(self):
        return self.question
    
class Evaluate(models.Model):
    fkuser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fktest = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    point = models.IntegerField()
    choice = (('Đ','Đ'),('CĐ','CĐ'))
    evaluate = models.CharField(choices=choice,max_length=2,default='CĐ')

    