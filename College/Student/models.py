from django.db import models

# Create your models here.
class Student_Register(models.Model):
     branches = (
         ('ece','ECE'),
         ('cse','CSE'),
         ('it','IT'),
         ('mech',"MECH")
     )

     First_name = models.CharField(max_length=20)
     Last_name =  models.CharField(max_length=20,blank=True,null=True)
     Roll_no = models.CharField(max_length=20)
     Branch = models.CharField(max_length=5,choices=branches)
     Email = models.EmailField(unique=True)
     Phone = models.CharField(max_length=10,help_text='Enter 10 digit mobile number')

     def __str__(self):
         return self.Roll_no

     class Meta:
        db_table = "Students_data"

class Library(models.Model):
    depts = (
        ('ece','ECE'),
         ('cse','CSE'),
         ('it','IT'),
         ('mech',"MECH"),
         ('chem','CHEM')
    )
    Book_name = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Department = models.CharField(max_length=10,choices=depts)
    Publication_date =  models.DateField()

    def __str__(self):
        return self.Book_name