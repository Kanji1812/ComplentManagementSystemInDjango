from django.db import models

class Type(models.Model):
    type_name = models.CharField(max_length=25)
    def __str__(self):
        return self.type_name
    
class department(models.Model):
    dept_name = models.CharField(max_length=25)
    def __str__(self):
        return self.dept_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=25)
    dept_name=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.subject_name 
    
SEMESTER_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F")
)
    
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=50)
    department = models.ForeignKey(department,on_delete=models.CASCADE,db_column='department')
    enrollment_no = models.IntegerField()
    email = models.EmailField(unique=True)
    Div = models.CharField(max_length=1,choices = SEMESTER_CHOICES,
        default = 'A')
    Roll_no =models.IntegerField(null=True)
    password = models.CharField(max_length=100)
    type_data =models.ForeignKey(Type,on_delete=models.CASCADE,db_column='type_data')
    def __str__(self):
        return self.s_name 

class Faculty(models.Model):
    faculty_name= models.CharField(max_length=70)
    email = models.EmailField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    department_name = models.ForeignKey(department,on_delete=models.CASCADE , db_column='department_name')
    type =models.ForeignKey(Type,on_delete=models.CASCADE , db_column='type')
    password = models.CharField(max_length=70,null=True)
    def __str__(self):
        return self.faculty_name  

class HOD(models.Model):
    hod_Name =models.CharField(max_length=55)
    email = models.EmailField()
    dept = models.ForeignKey(department,on_delete=models.CASCADE , db_column='dept')
    type = models.ForeignKey(Type,on_delete=models.CASCADE ,db_column='type')
    password = models.CharField(max_length=50)
    class Meta:
        db_table ='HOD'
    def __str__(self):
        return self.hod_Name
    
class Director(models.Model):
    director_name = models.CharField(max_length=55)
    email =models.EmailField(unique=True)
    password =models.CharField(max_length=55)
    type = models.ForeignKey(Type,on_delete=models.CASCADE ,db_column='type')
    class Meta:
        db_table = 'director'
    def __str__(self):
        return self.director_name

    
STATUS_CHOICES = (
("No Action", "No Action"),
("Accept", "Accept"),
("Closed", "Closed"),
("Escalated", "Escalated")
)

class Complaint(models.Model):
    sender =models.ForeignKey(Student,on_delete=models.CASCADE , db_column='sender')
    receiver=models.ForeignKey(Faculty,on_delete=models.CASCADE , db_column='receiver')
    subject = models.CharField(max_length=50 ,null=True)
    message= models.TextField(max_length=200)
    status = models.CharField( choices = STATUS_CHOICES,
        default = 'No Action',max_length=10 )
    user_type =models.ForeignKey(Type,on_delete=models.CASCADE,null=True,db_column='user_type')
    class Meta:
        db_table ='Complaint'
    def __str__(self):
       return self.subject
 