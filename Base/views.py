from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages, admin
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .form import *
from .models import *

# Create your views here.

def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    print(q)
    subjects = Subject.objects.filter(
        Q(fkctdt__name__icontains=q) |
        Q(name__icontains=q)
    )
    # users = User.objects.filter(
    #     Q(name__icontains=q)
    # )
    users = User.objects.all()
    nav_majors = Major.objects.all()
    
    subject_count = subjects.count()
    context = {'subjects': subjects,'subject_count':subject_count,
                'nav_majors': nav_majors,'users': users}

    return render(request,'base/home.html',context)

def Search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    print(q)
    subjects = Subject.objects.filter(
        Q(fkctdt__name__icontains=q) |
        Q(name__icontains=q)
    )
    # users = User.objects.filter(
    #     Q(name__icontains=q)
    # )
    users = User.objects.all()
    nav_majors = Major.objects.all()
    
    subject_count = subjects.count()
    context = {'subjects': subjects,'subject_count':subject_count,
                'nav_majors': nav_majors,'users': users}

    return render(request,'base/home.html',context)

def Login(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Người dùng không tồn tại')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Tài khoản hoặc mật khẩu không chính xác!!')

    context = {'page': page}
    return render(request, 'base/login.html', context)

def Register(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Đã xảy ra lỗi trong quá trình đăng ký')
    return render(request, 'base/login.html', {'form': form})
    
def Logout(request):
    logout(request)
    return redirect('home')

# @login_required(login_url='login')
# def updateUser(request):
#     user = request.user
#     form = UserForm(instance=user)

#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('user-profile', pk=user.id)

#     return render(request, 'base/update_user.html', {'form': form})

@login_required(login_url='login')
def CtdtMajor(request,pk):
    majors = Major.objects.get(id = pk)
    nav_majors = Major.objects.all()
    ctdts = Ctdt.objects.all()
    context = {'majors':majors,'ctdts':ctdts,'nav_majors':nav_majors}
    return render(request, 'base/major.html',context)

@login_required(login_url='login')
def SubjectCb(request,pk):
    page = 'subjectcb'
    majors = Major.objects.get(id = pk)
    nav_majors = Major.objects.all()
    ctdts = Ctdt.objects.all()
    # subjects = Subject.objects.all()
    # subject_count = subjects.count()
    context = {'majors':majors,'ctdts':ctdts,'nav_majors':nav_majors,'page':page}
    return render(request, 'base/subjectcb.html',context)

@login_required(login_url='login')
def SubjectCs(request,pk):
    page = 'subjectcs'
    majors = Major.objects.get(id = pk)
    nav_majors = Major.objects.all()
    ctdts = Ctdt.objects.all()
    # subjects = Subject.objects.all()
    # subject_count = subjects.count()
    context = {'majors':majors,'ctdts':ctdts,'nav_majors':nav_majors,'page':page}
    return render(request, 'base/subjectcb.html',context)

@login_required(login_url='login')
def SubjectCn(request,pk):
    majors = Major.objects.get(id = pk)
    nav_majors = Major.objects.all()
    ctdts = Ctdt.objects.all()
    # subjects = Subject.objects.all()
    # subject_count = subjects.count()
    context = {'majors':majors,'ctdts':ctdts,'nav_majors':nav_majors}
    return render(request, 'base/subjectcb.html',context)

@login_required(login_url='login')
def ListSubject(request,pk):
    form = SubjectForm()
    nav_majors = Major.objects.all()
    ctdts = Ctdt.objects.get(id = pk)
    subjects = Subject.objects.all()
    user = request.user
    if request.method == 'POST':
        Subject.objects.create(
            host = user,
            fkctdt = ctdts,
            name = ctdts.name,
            numsub = request.POST.get('numsub')
        )

    context = {'form': form,'ctdts':ctdts,'subjects':subjects,'nav_majors':nav_majors}
    return render(request, 'base/listsubject.html',context)

@login_required(login_url='login')
def ContentSubject(request,pk):
    chapterform = ChapterForm()
    testform = TestForm()
    nav_majors = Major.objects.all()
    subjects = Subject.objects.get(numsub = pk)
    subjectss = Subject.objects.all()
    chapters = Chapter.objects.all()
    tests = Test.objects.all()
    if request.method == 'POST':
        add = request.POST
        action = add.get('add')
        # print(action)
        if action == 'addchapter':
            Chapter.objects.update_or_create(
                fksubject = subjects,
                name = request.POST.get('name')
            )
            return redirect('contentsubject', pk=pk)
        elif action == 'addtest':
            Test.objects.update_or_create(
                fksubject = subjects,
                name = request.POST.get('name')
            )
            return redirect('contentsubject', pk=pk)
    else:
        testform = TestForm()
        chapterform = ChapterForm()
    context = {'testform':testform,'chapterform':chapterform,'nav_majors':nav_majors,'subjects':subjects,'subjectss':subjectss,'chapters':chapters,'tests':tests}
    return render(request, 'base/contentsubject.html',context)

# def AddChapter(request,pk):
#     subjects = Subject.objects.get(numsub = pk)
#     chapterform = ChapterForm()
#     if request.method == 'POST':
#         Chapter.objects.update_or_create(
#             fksubject = subjects,
#             name = request.POST.get('name')
#         )
#         return redirect('contentsubject', pk=pk)
#     else:
#         chapterform = ChapterForm()
#     context = {'chapterform':chapterform,'subjects':subjects}
#     return render(request, 'base/contentsubject.html',context)
@login_required(login_url='login')
def addFile(request,pk):
    form = FileForm()
    chapters = Chapter.objects.get(id=pk)
    nav_majors = Major.objects.all()
    files = File.objects.all()
    
    if request.method == 'POST':
        File.objects.update_or_create(
            fkchapter= chapters,
            file= request.FILES['file']
        )
    
    context = {'form':form,'chapters':chapters,'nav_majors':nav_majors,'files':files}
    return render(request, 'base/file.html',context)

@login_required(login_url='login')
def delFile(request,pk):
    page = 'delfile'
    nav_majors = Major.objects.all()
    files = File.objects.get(id=pk)
    pkchapter = files.fkchapter.id
    print(pkchapter)
    if request.method == 'POST':
        files.delete()
        return redirect('addfile', pkchapter)
    return render(request, 'base/del.html',{'files': files,'page':page,'nav_majors':nav_majors})

@login_required(login_url='login')
def delChapter(request,pk):
    page = 'delchapter'
    nav_majors = Major.objects.all()
    chapters = Chapter.objects.get(id = pk)
    fksub = chapters.fksubject.numsub
    if request.method == 'POST':
        chapters.delete()
        return redirect('contentsubject',fksub)
    return render(request, 'base/del.html',{'page':page,'chapters': chapters,'nav_majors':nav_majors})

@login_required(login_url='login')
def delTest(request,pk):
    page = 'deltest'
    nav_majors = Major.objects.all()
    tests = Test.objects.get(id = pk)
    fksub = tests.fksubject.numsub
    if request.method == 'POST':
        tests.delete()
        return redirect('contentsubject',fksub)
    return render(request, 'base/del.html',{'tests': tests,'nav_majors':nav_majors,'page':page})

@login_required(login_url='login')
def delQuest(request,pk):
    nav_majors = Major.objects.all()
    quests = ChoiceQuiz.objects.get(id = pk)
    fktest = quests.fktest.id
    # print(fktest)
    if request.method == 'POST':
        quests.delete()
        return redirect('test',fktest)
    return render(request, 'base/del.html',{'quests': quests,'nav_majors':nav_majors})

@login_required(login_url='login')
def PageTest(request,pk):
    nav_majors = Major.objects.all()
    if request.method == 'POST':
        add = request.POST
        action = add.get('add')
        if action == 'sumbit':
            user = request.user
            questionForm = QuestionForm()
            evaluates = EvaluateForm()
            questions = ChoiceQuiz.objects.all()
            tests = Test.objects.get(id = pk)
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                if q.fktest == tests:
                    total+=1
                    # print(request.POST.get(q.question))
                    # print(q.ans)
                    # print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=1
                        correct+=1
                    else:
                        wrong+=1
            percent = score/total *100
            Evaluate.objects.create(
                fkuser = user,
                fktest = tests,
                point = score
            )
            context = {
                'score':score,
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total,
                'nav_majors':nav_majors,
                'tests':tests
            }
            return render(request,'base/result.html',context)
        elif action == 'addquestion':
            tests = Test.objects.get(id = pk)
            ChoiceQuiz.objects.update_or_create(
                fktest = tests,
                question = request.POST.get('question'),
                op1 = request.POST.get('op1'),
                op2 = request.POST.get('op2'),
                op3 = request.POST.get('op3'),
                op4 = request.POST.get('op4'),
                ans = request.POST.get('ans'),
            )
            questionForm = QuestionForm()
            questions = ChoiceQuiz.objects.all()
            context = {'tests':tests,'questions':questions,'questonForm':questionForm,'nav_majors':nav_majors}
            return render(request, 'base/test.html',context)
    else:
        tests = Test.objects.get(id = pk)
        questionForm = QuestionForm()
        questions = ChoiceQuiz.objects.all()
        context = {'tests':tests,'questions':questions,'questionForm':questionForm,'nav_majors':nav_majors}
        return render(request, 'base/test.html',context)
    
    