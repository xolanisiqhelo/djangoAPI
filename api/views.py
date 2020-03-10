from rest_framework import generics, viewsets
from .models import approvals
from .serializer import approvalsSerializers
from sklearn.externals import joblib
import pandas as pd
from .form import ApprovalsForm
from django.shortcuts import render
from keras import backend as K
from django.contrib import messages


# Create your views here.

class approvalsList(generics.ListCreateAPIView):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers


class approvalsDetils(generics.RetrieveUpdateDestroyAPIView):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers


class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers


def ohevalue(df):
    ohe_col = joblib.load("/folder/APIs/django/djangoAPI/api/allcol.pkl")
    cat_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf


# @api_view(["POST"])
def approvereject(unit):
    try:
        mdl = joblib.load("/folder/APIs/django/djangoAPI/api/loan_model.pkl")
        scalers = joblib.load("folder/APIs/django/djangoAPI/api/scalers.pkl")
        X = scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred > 0.58)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({True: 'Approved', False: 'Rejected'})
        K.clear_session()
        return newdf.values[0][0], X[0]
    except ValueError as e:
        return (e.args[0])


def cxcontact(request):
    form = ApprovalsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Firstname = form.cleaned_data['Firstname']
            Lastname = form.cleaned_data['Lastname']
            Dependants = form.cleaned_data['Dependants']
            Applicantincome = form.cleaned_data['Applicantincome']
            Coapplicatincome = form.cleaned_data['Coapplicatincome']
            Loanamt = form.cleaned_data['Loanamt']
            Loanterm = form.cleaned_data['Loanterm']
            Credithistory = form.cleaned_data['Credithistory']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            # Graduatededucation = form.cleaned_data['graduatededucation']
            #    Selfemployed = form.cleaned_data['selfemployed']
            Property_Area = form.cleaned_data['Property_Area']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            print(approvereject(ohevalue(df)))
            answer = approvereject(ohevalue(df))[0]
            Xscalers = approvereject(ohevalue(df))[1]
            print(Xscalers)
            messages.success(request, 'Application Status: {}'.format(answer))
    else:
        form = ApprovalsForm()
    return render(request, 'myform/myform.html', {'form': form})
