from django.db import models


class ManagerModel(models.Model):
    managerID = models.IntegerField(primary_key=True)
    managerName = models.CharField(max_length=50)

    def __str__(self):
        return '{} ,{}'.format(str(self.managerID), self.managerName)


class DepartmentModel(models.Model):
    DepartmentID = models.IntegerField(primary_key=True)
    DepartmentName = models.CharField(max_length=50)
    managerModel = models.ForeignKey(ManagerModel, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(str(self.DepartmentID), self.DepartmentName)


class EmployeeModel(models.Model):
    title_ = (('Mr', 'Mr'), ('Mrs', 'Mrs'))
    employeeID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=10, choices=title_)
    employeeName = models.CharField(max_length=50)
    managerModel = models.ForeignKey(ManagerModel, on_delete=models.CASCADE)
    departmentModel = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(str(self.EmployeeID), self.EmployeeName)

