from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # path('Admin/', admin.site.urls, name='admin'),
    path('',views.Home,name="home"),
    path('TimKiem/',views.Search,name="search"),
    path('DangNhap/',views.Login,name="login"),
    path('DangKy/',views.Register,name="register"),
    path('DangXuat/',views.Logout,name="logout"),
    path('ChuongTrinhDaoTao/<str:pk>',views.CtdtMajor,name="major"),
    path('CoBan/<str:pk>',views.SubjectCb,name="subjectcb"),
    path('CoSo/<str:pk>',views.SubjectCs,name="subjectcs"),
    path('ChuyenNganh/<str:pk>',views.SubjectCn,name="subjectcn"),
    path('MonHoc/<str:pk>',views.ListSubject,name="listsubject"),
    path('NoiDungMonHoc/<str:pk>',views.ContentSubject,name="contentsubject"),
    path('TaiLieu/<str:pk>',views.addFile,name="addfile"),
    path('XoaFile/<str:pk>',views.delFile,name="delfile"),
    path('XoaChuong/<str:pk>',views.delChapter,name="delchapter"),
    path('XoaBaiKiemTra/<str:pk>',views.delTest,name="deltest"),
    path('XoaCauHoi/<str:pk>',views.delQuest,name="delquest"),
    path('BaiKiemTra/<str:pk>',views.PageTest,name="test"),
    path('KetQua/<str:pk>',views.PageTest,name="result"),
]
