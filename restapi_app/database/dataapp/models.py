from django.db import models

# Create your models here.
class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()
    class Meta:
        db_table = 'employees'
    def __str__(self):
        return self.first_name

class Departments(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=10)
    dept_name = models.CharField(unique=True, max_length=40)
    class Meta:
        db_table = 'departments'
    def __str__(self):
        return self.dept_name

class DeptEmp(models.Model):
    emp_no = models.OneToOneField('Employees', models.DO_NOTHING,      db_column='emp_no', primary_key=True)
    dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()
    class Meta:
        db_table = 'dept_emp'
        unique_together = (('emp_no', 'dept_no'),)

class DeptManager(models.Model):
    emp_no = models.OneToOneField('Employees', models.DO_NOTHING,   db_column='emp_no', primary_key=True)
    dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()
    class Meta:
        db_table = 'dept_manager'
        unique_together = (('emp_no', 'dept_no'),)

class Salaries(models.Model):
    emp_no = models.OneToOneField(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    class Meta:
        db_table = 'salaries'
        unique_together = (('emp_no', 'from_date'),)

class Titles(models.Model):
    emp_no = models.OneToOneField(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    class Meta:
        db_table = 'titles'
        unique_together = (('emp_no', 'title', 'from_date'),)




