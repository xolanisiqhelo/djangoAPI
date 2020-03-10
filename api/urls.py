from django.urls import path
from api import views

urlpatterns = [

    path('list/', views.approvalsList.as_view()),
    path('details/<int:pk>/', views.approvalsDetils.as_view()),
    path('status/', views.approvereject),
    path('form/', views.cxcontact, name="cxform")
]
