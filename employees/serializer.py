from rest_framework import serializers
from .models import DepartmentModel, EmployeeModel, ManagerModel


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = "__all__"


class ManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ManagerModel
        fields = "__all__"


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = "__all__"
