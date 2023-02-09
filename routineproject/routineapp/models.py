from django.db import models


class Teacher(models.Model):
    t_name = models.CharField(max_length=40)

    def __str__(self):
        return self.t_name


class Department(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=30)
    course_name = models.CharField(max_length=50)
    total_class = models.PositiveIntegerField()
    course_credit = models.DecimalField(max_digits=5, decimal_places=2)
    t_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Routine(models.Model):
    date = models.DateField()
    t_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return str(self.course_name)
