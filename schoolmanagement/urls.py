"""
by sumit kumar
written by fb.com/sumit.luv

"""
from django.contrib import admin
from django.urls import path
from school import views

from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('teacherclick', views.teacherclick_view),
    path('studentclick', views.studentclick_view),
    path('panchayathsecretaryclick', views.panchaythsecretaryclick_view),
    path('phcclick', views.phcclick_view),


    path('adminsignup', views.admin_signup_view),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('teachersignup', views.teacher_signup_view),
    path('adminlogin', LoginView.as_view(template_name='school/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='school/studentlogin.html')),
    path('teacherlogin', LoginView.as_view(template_name='school/teacherlogin.html')),
    path('phclogin', LoginView.as_view(template_name='school/phclogin.html')),
    path('panchayathsecretarylogin', LoginView.as_view(template_name='school/panchayathsecretarylogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='school/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
    path('admin-add-teacher', views.admin_add_teacher_view,name='admin-add-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view,name='admin-view-teacher'),
    path('admin-approve-teacher', views.admin_approve_teacher_view,name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher_view,name='delete-teacher'),
    path('delete-teacher-from-school/<int:pk>', views.delete_teacher_from_school_view,name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>', views.update_teacher_view,name='update-teacher'),
    path('admin-view-teacher-salary', views.admin_view_teacher_salary_view,name='admin-view-teacher-salary'),
     path('ashaview', views.asha_view,name='ashaview'),
     path('ashaview2', views.kid_view,name='ashaview2'),
path('ashaview3', views.vacc_view,name='ashaview3'),
    path('admin-student', views.admin_student_view,name='admin-student'),
    path('teacher-student', views.teacher_student_view,name='teacher-student'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),
    path('teacher-add-student', views.teacher_add_student_view,name='teacher-add-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('teacher-view-student', views.teacher_view_student_view,name='teacher-view-student'),
    path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('update-student-teacher/<int:pk>', views.update_student_teacher_view,name='update-student-teacher'),
    path('delete-student-teacher/<int:pk>', views.delete_student_teacher_view,name='delete-student-teacher'),
    path('admin-approve-student', views.admin_approve_student_view,name='admin-approve-student'),
    path('teacher-approve-student', views.teacher_approve_student_view,name='teacher-approve-student'),
    path('approve-student/<int:pk>', views.approve_student_view,name='approve-student'),
    #path('approve-student2/<int:pk>', views.approve_student_view2,name='approve-student2'),
    path('admin-view-student-fee', views.admin_view_student_fee_view,name='admin-view-student-fee'),


    path('admin-attendance', views.admin_attendance_view,name='admin-attendance'),
    path('admin-take-attendance/<str:cl>', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance/<str:cl>', views.admin_view_attendance_view,name='admin-view-attendance'),


    path('admin-fee', views.admin_fee_view,name='admin-fee'),
    path('admin-view-fee/<str:cl>', views.admin_view_fee_view,name='admin-view-fee'),

    path('admin-notice', views.admin_notice_view,name='admin-notice'),



    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
    path('teacher-attendance', views.teacher_attendance_view,name='teacher-attendance'),
    path('teacher-take-attendance/<str:cl>', views.teacher_take_attendance_view,name='teacher-take-attendance'),
    path('teacher-view-attendance/<str:cl>', views.teacher_view_attendance_view,name='teacher-view-attendance'),
    path('teacher-notice', views.teacher_notice_view,name='teacher-notice'),

    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('student-attendance', views.student_attendance_view,name='student-attendance'),

    path('phc-view-student', views.phc_view_student_view,name='phc-view-student'),
    path('phc-dashboard', views.phc_dashboard_view,name='phc-dashboard'),
    path('phc-view-teacher', views.phc_view_teacher_view,name='phc-view-teacher'),

    path('panchayathsecretary-dashboard', views.panchayathsecretary_dashboard_view,name='panchayathsecretary-dashboard'),
    path('panchayathsecretary-view-teacher', views.panchayathsecretary_view_teacher_view,name='panchayathsecretary-view-teacher'),
    path('panchayathsecretary-view-student', views.panchayathsecretary_view_student_view,name='panchayathsecretary-view-student'),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('student-message', views.student_message_view,name='student-message'),
     path('teacher-view-student-messages', views.teacher_view_student_feedback_view,name='teacher-view-student-messages'),
    path('student-edit', views.student_edit_view,name='student-edit'),
    path('preganancy-form', views.preg_view,name='preganancy'),
    path('kids-form', views.kids_view,name='kid'),
    path('covid-form', views.vacc_add,name='vacc'),


    path('admin-covidcases',views.viewcovid,name='admin-covidcases'),
    path('coviddatewise',views.viewcoviddatewise,name='coviddatewise'),
    path('covidfuture',views.viewcovidfuture,name='covidfuture'),
    path('covidoutbreaks',views.viewcovidoutbreak,name='covidoutbreaks'),

    

   
]
    
