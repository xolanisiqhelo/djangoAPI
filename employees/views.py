from django.shortcuts import render
from .models import ManagerModel, EmployeeModel, DepartmentModel
from .serializer import DepartmentSerializers, EmployeeSerializers, ManagerSerializers
from rest_framework import generics
from .form import DepartmentForm, EmployeeForm, ManagerForm
from django.contrib import messages




class DepartmentList(generics.ListCreateAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializers


class DepartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializers


class EmployeeList(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializers


class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializers


class ManagerList(generics.ListCreateAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializers


class ManagerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializers


def manager(request):
    form = ManagerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            managerID = form.cleaned_data['managerID']
            managerName = form.cleaned_data['managerName']
            form.save()
            messages.success(request, f'we have created manager successfully')

        else:
            form = ManagerForm
    return render(request, 'manager/manager.html', {'form': form})


def department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
            DepartmentID = form.cleaned_data['DepartmentID']
            DepartmentName = form.cleaned_data['DepartmentName']
            managerModel = form.cleaned_data['managerModel']
            print('this is the form')
            form.save()
            messages.success(request, f'we have created department successfully')

    return render(request, 'department/department.html', {'form': form})


def employee(request):
    form = EmployeeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            employeeID = form.cleaned_data['employeeID']
            title = form.cleaned_data['title']
            employeeName = form.cleaned_data['employeeName']
            managerModel = form.cleaned_data['managerModel']
            departmentModel = form.cleaned_data['departmentModel']
            messages.success(request, f'we have created employee successfully')
        else:
            form = EmployeeForm
    return render(request, 'employee/employee.html', {'form': form})



