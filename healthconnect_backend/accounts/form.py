from django import forms

class PatientCreateForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    dob = forms.DateTimeField()
    address = forms.CharField(max_length=100)
    mobile_no = forms.CharField(max_length=15)
    gender = forms.CharField(max_length=10)

class DoctorCreateForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    dob = forms.DateTimeField()
    address = forms.CharField(max_length=100)
    mobile_no = forms.CharField(max_length=15)
    gender = forms.CharField(max_length=10)
    qualification = forms.CharField(max_length=50)
    registration_no = forms.CharField(max_length=20)
    year_of_registration = forms.DateTimeField()
    state_medical_council = forms.CharField(max_length=50)
    specialization = forms.CharField(max_length=30)