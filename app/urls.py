from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='add_department'),
    path('adddepartment/',views.adddepartment,name='adddept'),
    path('showdept/',views.showdept,name='showdept'),
    path('del_dept/<int:id>',views.del_dept,name= 'del_dept'),
    path('fatch_dept/<int:id>',views.fatch_dept), 
    path('edit_dept/',views.edit_dept,name='editdept'),
    path('home/',views.home,name='home'),
    # This is a CRUd in Type Model.
    path("disp_type_form/",views.type_disp, name="disp_from"),
    path("addtype/",views.addtype, name="addtype"),
    path("showtype/",views.showtype, name="show_type"),
    path("del_type/<int:id>",views.del_type, name="deltype"),
    path("fatch_type/<int:id>",views.fatch_type, name="fetch_type"),
    path("edittype/",views.edit_type, name="edit_type"),

    # This is a Crud in Subject.
    path("addsubject/",views.add_subject, name="add_subject"),
    path("showsubject/",views.showsubject, name="showsubject"),
    path("del_subject/<int:id>",views.del_subject, name="add_subject"),
    path("fatchsubject/<int:id>",views.fatch_subject, name="fatch_subject"),
    path('editsubject/',views.edit_subject , name='edit_subject'),


    # this is a CRUD on Student.
    path('student_form/',views.form_student,name='reg'),
    path('store_data',views.store_student,name ='store_student'),
    path("showstudent/",views.show_stu ,name="show_student"),
    path("del_student/<s_id>",views.del_student),
    path("fatch_student/<int:s_id>",views.fatch_student),
    path("updatestudent/<int:s_id>",views.update_student),
   

    
    # this is a CRUD on Faculty.
    path("faculty_form/",views.faculty_from, name="facultyform"),
    path("add_faculty/",views.add_faculty, name="addfaculty"),
    path("show_faculty/",views.show_faculty, name="showfaculty"),
    path("del_faculty/<int:id>",views.del_faculty),
    path("edit_faculty/<int:id>",views.fatch_faculty,name='fatch_faculty'),
    path('updatefaculty/<int:id>',views.update_faculty),

    # This is a CRUD Complaint.
    path("add_complaint/",views.complaintform,name='add_complaent'),
    path("store_complaint/",views.store_complaint, name="store_comp"),
    path("show_complaint/",views.show_complaint, name="showcomplaint"),
    path("del_complaint/<int:id>",views.del_complaint, name="delete"),
    path("fatch_comp/<int:id>",views.fatch_complaint),
    path('login/',views.login,name='login'),
    
    path("moj/",views.moj, name="moj"),
    # This is the use for filter data for the perticular faculty.
    path("show_com/<name>", views.fileter_complant),
   

    # This is a CRUD in HOD.
    path('hod_form/',views.add_hod_form,name='add_hod'),
    path("addhod/",views.addhod, name="addhod"),
    path('show_hod/',views.showhod,name='show_hod'),
    path("del-HOD/<int:id>",views.delHOD, name="deleteHod"),
    path("hod_factch/<int:id>",views.factch_hod, name="factch_hod"),
    path("update_hod/<int:id>",views.update_hod),

    # this a CRUD on Director.
    path('show_director_form/',views.director_from,name='form_director'),
    path('stor_director/',views.storedata,name='stor_director'),
    path('show_director/',views.show_director,name='director_disp'),
    path('logout/',views.logout,name='logout'),

    # this is only for test.
    path('table/',views.table,name='table'),
    path('profile/',views.profile,name='profile'),
    path('homePage/',views.homepage),
    
]