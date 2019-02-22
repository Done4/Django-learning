from django.contrib import admin

# Register your models here.

from .models import Grades,Students

#关联对象 创建一个班级时 一起创建学生
class StudentsInfo(admin.TabularInline): #StackedInline
    model=Students
    extra =3 #创建两个学生

@admin.register(Grades)
class GreadesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo] #关联
    #显示字段
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    #过滤器
    list_filter = ['gname']
    #检索字段
    search_fields = ['gname','pk']
    #分页 一页显示几条
    list_per_page = 5
    #改变添加、修改页面的属性 顺序
    #fields = ['gdate','ggirlnum','gboynum','isDelete','gname']
    #属性分组 不能和fields 同时使用
    fieldsets = [('num',{'fields':['ggirlnum','gboynum']}),('base',{'fields':['gname','gdate','isDelete']})]
    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True
#admin.site.register(Grades,GradesAdmin)

#使用装饰器注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    #设置页面列的名称
    gender.short_description = '性别'
    list_display = ['pk','sname',gender,'sage','scontend','isDelete','sgrade']
    list_per_page = 3
    #执行动作的位置
    actions_on_top =False
    actions_on_bottom = True
#admin.site.register(Students,StudentsAdmin)