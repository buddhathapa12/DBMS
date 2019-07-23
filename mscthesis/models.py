from django.db import models

# Create your models here.
class Student(models.Model):
    batch = models.CharField(max_length = 5)
    department = models.CharField(max_length = 5)
    class_rollno = models.CharField(max_length = 5)
    first_name = models.CharField(max_length = 20)
    middle_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)

    class Meta:
        unique_together = ('batch', 'department', 'class_rollno')

class Supervisor(models.Model):
    title = models.CharField(max_length = 15)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Area(models.Model):
    NAME = [
        (1,'Big Data'),
        (2,'Bioinformatics'),
        (3,'Cloud Computing'),
        (4,'Data Analysis'),
        (5,'GIS'),
        (6,'Image Processing'),
        (7,'IoT'),
        (8,'Machine Learning'),
        (9,'Networks/Security'),
        (10,'NLP and Semantics'),
    ]
    name = models.IntegerField(choices = NAME)


class Thesis(models.Model):
    student = models.OneToOneField(Student, on_delete= models.CASCADE)
    supervisor = models.ForeignKey(Supervisor,on_delete= models.CASCADE)
    area = models.ForeignKey(Area,on_delete= models.CASCADE)
    title = models.CharField(max_length = 250)



class Submission(models.Model):
    student = models.OneToOneField(Student ,on_delete= models.CASCADE )
    mid_term = models.DateField()
    final= models.DateField()

class Status(models.Model):
    student = models.OneToOneField(Student ,on_delete= models.CASCADE )
    mid_term_submitted= models.BooleanField(default= False)
    final_submitted= models.BooleanField(default= False)
    
