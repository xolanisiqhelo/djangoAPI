from django.urls import path
from employees import views

urlpatterns = [
    path('listEmp/', views.EmployeeList.as_view()),
    path('detailsEmp/<int:pk>/',views.EmployeeDetails.as_view()),
    path('listManager/', views.ManagerList.as_view()),
    path('detailsManager/<int:pk>/', views.ManagerDetails.as_view()),
    path('listDep/', views.DepartmentList.as_view()),
    path('detailsDep/<int:pk>/',views.DepartmentDetails.as_view()),
    path('', views.manager,name='manager-form'),
    path('departmentForm/', views.department,name='department-Form'),
    path('employeeForm/', views.employee ,name='employee-Form'),


]
