# This is matploatlib and numpy for pie chart.
import pandas as pd
import matplotlib.pyplot as plt


from django.shortcuts import render,HttpResponse,redirect
from .forms import departmentform,Typeform,facultyform,Director_form
from .forms import Subjectform,student_form,edit_faculty_form,edit_student,HOD_form,HOD_edit,complaint_form,edit_complaint_form
from .models import Student, department,Type,Subject,Faculty,Complaint,HOD,Director
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
# this is a all method are create for CRUD in department.
def login(request):
    if request.method =="POST":
        s_name = request.POST.get('s_name')
        password_login = request.POST.get('password')
        data = None
        try:
            data = Student.objects.get(s_name=s_name,password=password_login)
            request.session['name']= data.s_name
            request.session['type'] = data.type_data.type_name
            request.session['email'] = data.email
            # print(request.session.get('name'))
            if data is not None:
                return render(request,'home/index.html',{'name':request.session.get('name'),'email':request.session.get('email')})
            else:
                msg = 'The User is not Registered.'
                return render(request,'login.html',{'msg':msg})
        except:
            try:
                data = Faculty.objects.get(faculty_name=s_name,password=password_login)
                request.session['name']= data.faculty_name
                request.session['type'] = data.type.type_name
                request.session['email'] = data.email
                print(request.session.get('name'))
                if data is not None:
                    print(data.type)
                    return redirect('/moj/')
                else:
                    msg = 'The User is not Registered.'
                    return render(request,'login.html',{'msg':msg})
            except:
                try:
                    data = HOD.objects.get(hod_Name=s_name,password=password_login)
                    request.session['name']= data.hod_Name
                    request.session['type'] = data.type.type_name
                    request.session['email'] = data.email
                    print(request.session.get('name'))
                    if data is not None:
                        return redirect('/moj/')
                    else:
                        msg = 'The User is not Registered.'
                        return render(request,'login.html',{'msg':msg})
                except:
                    try:
                        data = Director.objects.get(director_name=s_name,password=password_login)
                        request.session['name']= data.director_name
                        request.session['type'] = data.type.type_name
                        request.session['email'] = data.email
                        print(request.session.get('name'))
                        if data is not None:
                            return redirect('/moj/')
                        else:
                            msg = 'The User is not Registered.'
                            return render(request,'login.html',{'msg':msg})
                    except:
                        return render(request,'login.html')
                
    else:
        return render(request,'login.html')
    

def welcome(request):
    form = departmentform(request.POST)
    return render (request,'department.html',{'form':form})


def adddepartment(request):
    if request.method == 'POST':
        form = departmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/showdept/")
        else:
            return HttpResponse('The data could not be saved in the database.')        
           
def showdept(request):
    data = department.objects.all()
    paginator = Paginator(data,2)
    try :
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request,'tables.html',{'students':posts,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})

def del_dept(request,id):
    data = department.objects.get(id=id)
    data.delete()
    return redirect("/showdept/")

def fatch_dept(request,id):
    data = department.objects.get(id=id)
    return render(request,'edit.html',{'data':data})

def edit_dept(request):
    id = request.POST.get('id')
    print(id)
    data = department.objects.get(id = id)
    form = departmentform(request.POST, instance = data)
    if form.is_valid:
        form.save()
        return redirect('/showdept/')
    return render(request,'edit.html',{'data':data})

# This is a Type Model CRUD.

def type_disp(request):
    form = Typeform(request.POST)
    return render(request,'type/addtype.html',{'form':form})
def addtype(request):
    if request.method == 'POST':
        form = Typeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/showtype/")
        else:
            return HttpResponse('The data could not be saved in the database.')        
def showtype(request):
    data = Type.objects.all()
    paginator = Paginator(data,2)
    try :
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request,'type/type_show.html',{'data':posts,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})

def del_type(request,id):
    data = Type.objects.get(id = id)
    data.delete()
    return redirect("/showtype/")
def fatch_type(request,id):
    data = Type.objects.get(id =id)
    return render(request,'type/edit_type.html',{'data':data})
def edit_type(request):
    id = request.POST.get('id')
    print(id)
    data = Type.objects.get(id = id)
    form = Typeform(request.POST, instance = data)
    if form.is_valid:
        form.save()
        return redirect('/showtype/')
    return render(request,'type/edit_type.html',{'data':data})

# ================================================================================

# this a CRUD for Subject

def add_subject(request):
    if request.method == 'POST':
        name = request.POST.get('subject_name')
        dept_id = request.POST.get('dept_name')
        dept_name = department.objects.get(id = dept_id)
        print(dept_name)
        Subject.objects.create(
             subject_name = name,
             dept_name = dept_name
        )
        return render(
            request,
            'subject/subject_show.html',
            {
                'dept': Subject.objects.all(),
                
            }
        )
    else :
        return render( request,'subject/addsubject.html',{'dept': department.objects.all()})

def showsubject(request):
    data = Subject.objects.all()
    paginator = Paginator(data,2)
    try :
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(
            request,
            'subject/subject_show.html',
            {
                'data':posts,
                'name':request.session.get('name'),
                'type':request.session.get('type'),
                'email':request.session.get('email'),
            }
        )

def del_subject(request,id):
    data = Subject.objects.get(id = id)
    data.delete()
    return render(
            request,
            'subject/subject_show.html',
            {
                'dept': Subject.objects.all(),
                
            }
        )

def fatch_subject(request,id):
    data = Subject.objects.get(id =id)
    return render(
        request,
        'subject/fatch_subject.html',
        {'data':data,
        'dept': department.objects.all()})

def edit_subject(request):
    id = request.POST.get('id')
    data = Subject.objects.get(id = id)
    form = Subjectform(request.POST, instance = data)
    if form.is_valid:
        form.save()
        return redirect('/showsubject/')
    return render(
        request,
        'subject/fatch_subject.html',
        {'data':data,
        'dept': Subject.objects.all()})

# this is CRUD of Student
def form_student(request):
    form = student_form()
    return render(request,'student/add_student.html',{'form':form})

# def add_student(request):
#     if request.method == 'POST':
#         data = student_form(request.POST)
#         if data.is_valid():
#             data.save()
#             return redirect('/showstudent/')
#         else:
#             return HttpResponse('the Data Is not Saved')


def store_student(request):
    if request.method == 'POST':
        name = request.POST.get('s_name')
        email= request.POST.get('email')
        password = request.POST.get('password')
        # print(password,name,email)
        data = None
        # data = Student.objects.get(s_name = name,email = email,password = password)
        if data is not None :
            form = student_form()
            return render(request,'student/add_student.html',{'form': form,'msg':'The User Is Allready Registered.'})
        else:
            form = student_form(request.POST)
            if form.is_valid():
                data = Type.objects.get(type_name = 'Student')
                # <!-- fields = ["s_name","enrollment_no","email","Div","Roll_no","password","department"] -->
                form = form.save(commit=False)
                form.s_name = name
                form.enrollment_no = request.POST.get('enrollment_no')
                form.email = email
                form.Roll_no = request.POST.get('Roll_no')
                form.password = request.POST.get('password')
                form.type_data = data
                form.save()
                return redirect("/login/")
            else:
                return HttpResponse('The data could not be saved in the database.')        
    else:
        return HttpResponse('the request is not post')
       
def show_stu(request):
    data = Student.objects.all()
    paginator = Paginator(data,3)
    try :
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request,'student/show_student.html',{'data':posts,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})
# this is a delete in STUDENT
def del_student(request,s_id):
    data = Student.objects.get(s_id=s_id)
    try:
        data.delete()
        return redirect("/showstudent/")
    except:
        return HttpResponse('the data is not deleted😂😊')
def fatch_student(request,s_id):
    course= Student.objects.get(s_id=s_id) 
    form = edit_student(instance = course)  
    return render(request,'student/edit_student.html', {'course':course,'form':form}) 

def update_student(request, s_id):  
    course = Student.objects.get(s_id=s_id)  
    print(course)
    form = edit_student(request.POST, instance = course)  
    print(form)
    if form.is_valid():  
        form.save() 
        return redirect("/showstudent/")  
    return HttpResponse('the data is not update')



# This is a CRUD In Faculty.
def faculty_from(request):
    form = facultyform()
    return render(request,'faculty/faculty_form.html',{'form':form,'name_of_form':'Add Faculty'})
  
'''def add_faculty(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('faculty_name')
            email= request.POST.get('email')
            password = request.POST.get('password')
            data = None
            data = Faculty.objects.filter(faculty_name = name,email = email,password = password)
            # print(type(data.email))
            print(data)
            if data is not None :
                form = facultyform()
                return render(request,'faculty/faculty_form.html',{'form': form,'msg':'The User Is Allready Registered.'})
        except: 
            form = facultyform(request.POST)
            if form.is_valid():
                data = Type.objects.get(type_name = 'FACULTY')
                # This is a for a test use 
                #  fields = ['faculty_name','email','subject','department_name','password'] 
                form = form.save(commit=False)
                form.type = data
                form.faculty_name= request.POST.get('faculty_name')
                form.email = request.POST.get('email')
                form.password = request.POST.get('password')
                print(request.POST.get('faculty_name'),request.POST.get('email',request.POST.get('password')))
                form.save()
                return redirect("/login/")
            else:
                return HttpResponse('The data could not be saved in the database.')        
       
 '''      
def add_faculty(request):
    print("Name Of Faculty"+request.POST.get("faculty_name"))
    print("The email Of Faculty",request.POST.get('email'))
    # print("This is a subject",request.POST.get('subject'))
    # print("This is a my department ",request.POST.get('department_name'))
    print("This is a Password Of it ",request.POST.get('password'))
    if request.method == 'POST':
        try:
            form = facultyform(request.POST)
            if form.is_valid():
                data = Type.objects.get(type_name = 'FACULTY')
                # This is a for a test use 
                #  fields = ['faculty_name','email','subject','department_name','password'] 
                form = form.save(commit=False)
                form.type = data
                form.faculty_name = request.POST.get('faculty_name')
                form.email = request.POST.get('email')
                form.password = request.POST.get('password')
                # print(request.POST.get('faculty_name'),request.POST.get('email',request.POST.get('password')))
                form.save()
                return redirect("/login/")
            else:
                return HttpResponse('The data could not be saved in the database.')        

        except: 
            return redirect("/")
            
       
       
       
def show_faculty(request):
    serche =request.POST.get('serche')
    # print(serche)
    if serche:
        try:
            data = Faculty.objects.filter(faculty_name = serche)
        except:
            try:
                data = Faculty.objects.filter(email = serche)
                print(data.faculty_name)
                return render(request,'faculty/show_faculty.html',{'data': data,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})
            except:
                pass
                
    data = Faculty.objects.all()
    paginator = Paginator(data,2)
    try :
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request,'faculty/show_faculty.html',{'data':posts})
    

def del_faculty(request,id):
    try:
        data = Faculty.objects.get(id=id)
        data.delete()
        return redirect('/show_faculty/')
    except:
        data = Faculty.objects.all()
        paginator = Paginator(data,2)
        try :
            page = int(request.GET.get('page','1'))
        except:
            page = 1
        try:
            posts = paginator.page(page)
        except(Paginator.EmptyPage , Paginator.InvalidPage):
            posts = paginator.page(paginator.num_pages)
        return render(request,'faculty/show_faculty.html',{'data':posts,'msg':"The Selected Recode is not Deleted"})
def fatch_faculty(request,id):
    course= Faculty.objects.get(id=id) 
    form = edit_faculty_form(instance = course)  
    return render(request,'faculty/edit_faculty.html', {'course':course,'form':form}) 

def update_faculty(request, id):  
    course = Faculty.objects.get(id=id)  
    print(course)
    form = edit_faculty_form(request.POST, instance = course)  
    print(form)
    if form.is_valid():  
        form.save() 
        return show_faculty(request)  
    return HttpResponse('the data is not update')

# This is a Complaint CRUD.

def complaintform(request):
    data= complaint_form()
    return render(request,'Complaint/add_complaint.html',{'form':data})
def store_complaint(request):
    if request.method == "POST":
        form = complaint_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show_complaint/")
        else:
            return HttpResponse('The data could not be saved in the database.')        

    else:
        return HttpResponse('the data is not Saved')
def show_complaint(request):
    serche =request.POST.get('serche')
    if serche:
        try:
            student_id = Student.objects.get(s_name = serche) 
            data = Complaint.objects.all().filter(sender = student_id)
        except:
            faculty_id =Faculty.objects.get(faculty_name = serche)
            data = Complaint.objects.all().filter(receiver = faculty_id)
        return render(request,'Complaint/show.html',{'data':data,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})        
    data = Complaint.objects.all()
    paginator = Paginator(data,5)
    try :
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request,'Complaint/show.html',{'data':posts,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})        
def del_complaint(request,id):
    data = Complaint.objects.get(id=id)
    try:
        data.delete()
        return redirect('/show_complaint/')
    except:
        data = Faculty.objects.all()
        paginator = Paginator(data,2)
        try :
            page = int(request.GET.get('page','1'))
        except:
            page = 1
        try:
            posts = paginator.page(page)
        except(Paginator.EmptyPage , Paginator.InvalidPage):
            posts = paginator.page(paginator.num_pages)
        return render(request,'faculty/show_faculty.html',{'data':posts,'msg':"The Selected Recode is not Deleted"})
def fatch_complaint(request,id):
    course= Complaint.objects.get(id=id) 
    form = edit_complaint_form(instance = course)  
    return render(request,'Complaint/edit.html', {'course':course,'form':form}) 


# This is a CRDU in HOD.
def add_hod_form(request):
    data =HOD_form()
    return render(request,'HOD/hod_form.html',{'form':data})

def addhod(request):
    if request.method == "POST":
        name = request.POST.get('hod_Name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            data =  None
            data = HOD.objects.get(hod_Name = name,email = email,password = password)
            if data is not None:
                data =HOD_form()
                return render(request,'HOD/hod_form.html',{'form':data , 'msg':'This Faculty Is allrady Registered.'})
        except:
            form = HOD_form(request.POST)
            if form.is_valid():
                form = form.save(commit = False)
                data = Type.objects.get(type_name ='HOD')
                form.type = data
                form.save()
                return redirect("/show_hod/")
            else:
                return HttpResponse('The data could not be saved in the database.')        
    else:
        return HttpResponse('the data is not Saved')
def showhod(request):
    data = HOD.objects.all()
    paginator = Paginator(data,2)
    try :
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request,'HOD/show_hod.html',{'data':posts,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})
    
def delHOD(request,id):
    data = HOD.objects.get(id=id)
    try:
        data.delete()
        return redirect('/show_hod/')
    except:
        data = Faculty.objects.all()
        paginator = Paginator(data,2)
        try :
            page = int(request.GET.get('page','1'))
        except:
            page = 1
        try:
            posts = paginator.page(page)
        except(Paginator.EmptyPage , Paginator.InvalidPage):
            posts = paginator.page(paginator.num_pages)
        return render(request,'HOD/show_hod.html',
                      {'data':posts,
                                    'name':request.session.get('name'),
                                    'type':request.session.get('type'),
                                    'email':request.session.get('email'),
                                    'msg':"The Selected Recode is not Deleted"})
def factch_hod(request,id):
    try:
        HOD_data= HOD.objects.get(id=id) 
        form = HOD_form(instance = HOD_data)  
        return render(request,'HOD/edit_HOD.html', {'course':HOD_data,'form':form}) 
    except:
        return redirect('/show_hod/')

def update_hod(request,id):
    data = HOD.objects.get(id=id)  
    form = HOD_edit(request.POST, instance = data)  
    print(form)
    if form.is_valid():  
        form.save() 
        return showhod(request)  
    return HttpResponse('the data is not update')

# This all Methods are for CRUd in Director.
def director_from(request):
    data = Director_form()
    return render(request,'Director/form_director.html',{'form':data})
# store Director
def storedata(request):
    if request.method == 'POST':
        form = Director_form(request.POST)
        try:
            name = request.POST.get('faculty_name')
            email = request.POST.get('email')
            subject = 'welcome to K and K Info-tech LTD'
            message = f'Hi i am {name}, thank you for registering in K and K Info Tech Limited.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
        except:
            pass
        if form.is_valid():
            typedata= Type.objects.get(type_name = 'DIRECTOR')
            formx = form.save(commit=False)
            formx.type = typedata
            formx.save()
            if formx:
                return redirect("/login/")    
        return HttpResponse('the data is not saved')
    else:
        return director_from(request) 
        
def del_director(request,id):
    try:
        data = Director.objects.get(id=id)
        data.delete()
        return 
        pass
    except:
        pass

def show_director(request):
    serche =request.POST.get('serche')
    if serche:
        try:
            data = Director.objects.filter(director_name = serche)  
        except:
            data = Director.objects.filter(email = serche)
        return render(request,'Complaint/show.html',{'data':data})        
    try:
        data = Director.objects.all()
        paginator = Paginator(data,5)
        try :
            page = int(request.GET.get('page','1'))
        except:
            page = 1
        try:
            posts = paginator.page(page)
        except(Paginator.EmptyPage , Paginator.InvalidPage):
            posts = paginator.page(paginator.num_pages)
        return render(request,'Director/show.html',{'data':posts,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})
    except:
        return redirect('/login/')


    #     if request.method == "POST":
    #     form = HOD_form(request.POST)
    #     if form.is_valid():
    #         form.save()
            
    #         return redirect("/show_hod/")
    #     else:
    #         return HttpResponse('The data could not be saved in the database.')        

    # else:
    #     return HttpResponse('the data is not Saved')


 # try:
        #     stu=Student.objects.get(s_id=request.POST.get('s_id',False))
        # except Student.DoesNotExist:
        #     stu=None
        # if stu:
        #     # messages.warning(request,"Sid Already Exists")
        #     return HttpResponse('the data is saved')
        # else:
        #     if form.is_valid():
        #         try:
        #             # phone_no = request.session.get('phone_no')
        #             user =CustomUser.objects.get(phone_no=phone_no)
        #             student = form.save(commit=False)
        #             student.user = user
        #             student.save()

        #             messages.success(request,"Data Stored Successful")
        #             return redirect("show_student.html")
        #         except:
        #             pass
        #     else:
        #         form= student_form()
        #         return render(request,'add_student.html',{'form': form})




def logout(request):
    del request.session['name']
    del request.session['type']
    del request.session['email']
    return redirect('/login/')





def home(request):
    return render(request,'index_1.html',{'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})


def reg(request):
    return render(request,'register.html')
def table(request):
    return render(request,'tables.html')
def profile(request):
    return render(request,'profile.html')
def homepage(request):
    return render(request,'index_home.html')
def moj(request):
    return render(request,'moj.html',{'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})

    # return render(request,")
    
    
    
    
def fileter_complant(request,name):
    print(name)
    
    serche = name
    if serche:
        faculty_id =Faculty.objects.get(faculty_name = serche)
        data = Complaint.objects.all().filter(receiver = faculty_id)
        return render(request,'Complaint/show.html',{'data':data,'name':request.session.get('name'),'type':request.session.get('type'),'email':request.session.get('email')})
    else :
        return redirect("/")
    