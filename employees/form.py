from django import forms
from .models import ManagerModel, DepartmentModel


class ManagerForm(forms.ModelForm):
    class Meta:
        model = ManagerModel
        fields = '__all__'
    # managerID = forms.IntegerField()
    # managerName = forms.CharField(max_length=50)

    # class ManagerForm(forms.Form):
    #     managerID = forms.IntegerField()
    #     managerName = forms.CharField(max_length=50)


class DepartmentForm(forms.Form):
    DepartmentID = forms.IntegerField()
    DepartmentName = forms.CharField(max_length=50)
    managerModel = forms.ModelMultipleChoiceField(queryset=ManagerModel.objects.all())


class EmployeeForm(forms.Form):
    employeeID = forms.IntegerField()
    title = forms.ChoiceField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs')])
    employeeName = forms.CharField(max_length=50)
    managerModel = forms.ModelMultipleChoiceField(queryset=ManagerModel.objects.all())
    departmentModel = forms.ModelMultipleChoiceField(queryset=DepartmentModel.objects.all())
