from django.contrib import admin
from  .models import  DepartmentModel,EmployeeModel,ManagerModel

# Register your models here.
admin.site.register(DepartmentModel)
admin.site.register(EmployeeModel)
admin.site.register(ManagerModel)

