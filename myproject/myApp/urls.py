from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^(\d+)',views.detail),
    url(r'^grades/$',views.grades),
    url(r'^students/$', views.students),

    url(r'^grades/(\d+)$',views.gradesStudents),
    url(r'^addstudent/$',views.addstudent),
    url(r'^stu/(\d+)$',views.stupage),
    url(r'^get1/$',views.get1),
    url(r'^register/$',views.register),
    url(r'^register/regist/$',views.regist),
    url(r'^redirect1',views.redirect1),
    url(r'^redirect2',views.redirect2),

    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^quit/$',views.quit),
    url(r'head/$',views.head)
]