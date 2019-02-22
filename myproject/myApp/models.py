from django.db import models

# Create your models here.
#不需要定义主键，在生成时自动添加
class Grades(models.Model):
    gname =models.CharField(verbose_name='班级名',max_length=20)
    gdate=models.DateTimeField(verbose_name='成立时间')
    ggirlnum=models.IntegerField(verbose_name='女生人数')
    gboynum=models.IntegerField(verbose_name='男生人数')
    isDelete=models.BooleanField(default=False,verbose_name='是否解散')
    def __str__(self):
        return self.gname


class StudentsManager(models.Manager):
    def get_queryset(self):
        #过滤
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)


class Students(models.Model):
    #自定义模型模型管理器 , 自定义以后 objects 就没了
   # stuObj=StudentsManager()
    sname=models.CharField(verbose_name='姓名',max_length=20)
    sgender=models.BooleanField(default=True)
    sage=models.IntegerField(verbose_name='年龄')
    scontend=models.CharField(verbose_name='简介',max_length=20)
    isDelete=models.BooleanField(verbose_name='是否存活',default=False)
    sgrade=models.ForeignKey('Grades',on_delete=models.CASCADE)#外键
    def __str__(self):
        return self.sname
    # class Meta:
    #     #表名
    #     db_table='students'
    #     #排序
    #     ordering =['id'] # 默认升序 ['-id'] 降序
    #

    #定义一个类方法创建对象
    @classmethod
    def createStudent(cls,name,gender,age,contend,grade,isD=False):
        stu=cls(sname=name,sgender=gender,sage=age,scontend=contend,sgrade=grade,isDelete=isD)
        return stu
