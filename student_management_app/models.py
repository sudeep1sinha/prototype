from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class User(models.Model):
    user=models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)


class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class Courses(models.Model):
    course_id=models.CharField(max_length=225)
    course_name=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Subjects(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=225)
    subject_code=models.CharField(max_length=225)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.subject_id

class Students(models.Model):
    semester_choice = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
        (6, 'Sixth'),
        (7, 'Seventh'),
        (8, 'Eighth'),
    )
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False, default='')
    semester = models.IntegerField(choices=semester_choice, null=False, default=1)
    phone = models.CharField(max_length=12, null=False, default='')
    gender=models.CharField(max_length=225, null=False , default='')
    email=models.CharField(max_length=225, null=False , default='')
    password=models.CharField(max_length=225, null=False , default='')
    address=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class NotificationStudents(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



