
from django.db import models
from django import forms

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    noOfQuestion = models.IntegerField()
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Department(models.Model):
    depName = models.CharField(max_length=100)
    employees = models.IntegerField()
    HOD = models.CharField(max_length=100)
    depPhone = models.CharField(max_length=15)
    depImail = models.EmailField()


class Employees(models.Model):  # Capitalize class name for consistency
    empName = models.CharField(max_length=100)
    salary = models.IntegerField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.empName

class Student(models.Model):  # Capitalize class name for consistency
    studentName = models.CharField(max_length=200)
    studentRollNo = models.IntegerField()
    collegeId = models.IntegerField()
    collegeName = models.CharField(max_length=300)
    subject1Marks = models.IntegerField()
    subject2Marks = models.IntegerField()
    subject3Marks = models.IntegerField()
    subject4Marks = models.IntegerField()
    subject5Marks = models.IntegerField()
    totalMarks = models.IntegerField()
    persentage = models.IntegerField()
    grade = models.CharField(max_length=1)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees  # Ensure the model name matches the class name
        fields = ['empName', 'salary', 'designation']  # Use correct field names

