from django import forms


class ApprovalsForm(forms.Form):
    Firstname = forms.CharField(max_length=15)
    Lastname = forms.CharField(max_length=15)
    Dependants = forms.IntegerField()
    Applicantincome = forms.IntegerField()
    Coapplicatincome = forms.IntegerField()
    Loanamt = forms.IntegerField()
    Loanterm = forms.IntegerField()
    Credithistory = forms.IntegerField()
    Gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    Married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    # Graduatededucation = forms.ChoiceField(choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate')])
    # Selfemployed = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Property_Area = forms.ChoiceField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])


