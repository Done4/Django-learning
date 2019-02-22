from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Grades,Students
#定义视图
def index(request):
    return HttpResponse('none---')

def detail(request,num):
    return HttpResponse('detail is %s'%num)

def grades(request):
    #去模型取数据
    gradesList=Grades.objects.all()
    #将数据传给模板,模板再渲染页面,渲染好的页面返回浏览器
    return render(request,'myApp/grades.html',{"grades":gradesList})

def students(request):
    #去模型取数据
    stusList=Students.objects.all()
    #将数据传给模板,模板再渲染页面,渲染好的页面返回浏览器
    return render(request,'myApp/students.html',{"students":stusList,"list":['a','b','c'],
                                                 "num":10
                                                 })

def gradesStudents(request,num):
    #获得对应的班级对象
    grade=Grades.objects.get(pk=num)
    #获得班级下的所有学生对象列表
    studentsList=grade.students_set.all()
    return render(request,'myApp/students.html',{"students":studentsList})

def addstudent(request):
    grade=Grades.objects.get(pk=1)
    stu=Students.createStudent('liangfeifan',True,10,'i am feifange',grade)
    stu.save()
    return HttpResponse('创建成功')
#分页显示
def stupage(request,page):
    page=int(page)
    stuList=Students.objects.all()[(page-1)*3:page*3]
    return render(request,'myApp/students.html',{'students':stuList})

def get1(request):
    s=request.GET.getlist('a')
    b=request.GET['b']#request.GET.get('b')
    return HttpResponse(s[0]+b)


def register(request):
    return render(request,'myApp/register.html')

def regist(request):
    name=request.POST.get('name')
    gender=request.POST.get('gender')
    age=request.POST.get('age')
    hobby=request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse('注册成功')

#重定向
from django.http import  HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(request):
    #return HttpResponseRedirect('/redirect2')
    return redirect('/redirect2')
def redirect2(request):
    return HttpResponse("我是重定向后的视图")

#返回json 数据 一般用于异步请求
from django.http import JsonResponse


def main(request):
    #取session 没取到值就是后面的参
    username=request.session.get('username','游客')

    return render(request,'myApp/main.html',{'username':username})

def login(request):
    return render(request,'myApp/login.html')
#不设置session 期限 两星期过期 ,可以用时间对象 ，写 0 关闭浏览器时失效,None 永不过期
def showmain(request):
    username=request.POST.get('username')
    #存储session
    request.session['username']=username
    #10秒过期
    request.session.set_expiry(10)
    return redirect('/main')
from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)
    #request.session.clear()
    #request.session.flush()
    return redirect('/main')
#继承实例
def head(request):
    return render(request,'myApp/head.html')
