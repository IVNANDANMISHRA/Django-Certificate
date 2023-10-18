from django.db import models

class Teacher(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    students = models.ManyToManyField('Student')

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    grade = models.CharField(max_length=2,default=0)
    teachers = models.ManyToManyField('Teacher')

    def __str__(self):
        return self.name

class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_text = models.TextField()

    def generate_certificate(self):
        self.certificate_text = f"Certificate of achievement for {self.student.name} in {self.teacher.name}"