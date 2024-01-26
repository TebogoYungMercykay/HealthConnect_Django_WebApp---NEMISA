from django import forms

class PatientCreateForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    dob = forms.DateField()
    address = forms.CharField(max_length=100)
    mobile_no = forms.CharField(max_length=15)
    gender = forms.CharField(max_length=10, widget=forms.Select(choices=[
        ('', 'Select your gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]), required=True)
    
    def clean_mobile_no(self):
        mobile_no = str(self.cleaned_data.get('mobile_no', '')).lstrip('0')
        try:
            mobile_no = int(mobile_no)
        except ValueError:
            raise forms.ValidationError('Mobile number must be a valid integer.')

        return mobile_no



class DoctorCreateForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    dob = forms.DateField()
    address = forms.CharField(max_length=100)
    mobile_no = forms.CharField(max_length=15)
    gender = forms.CharField(max_length=10, widget=forms.Select(choices=[
        ('', 'Select your gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]), required=True)
    qualification = forms.CharField(max_length=50)
    registration_no = forms.CharField(max_length=20)
    year_of_registration = forms.DateField()
    state_medical_council = forms.CharField(max_length=50)
    specialization = forms.CharField(max_length=30)
    
    def clean_mobile_no(self):
        mobile_no = str(self.cleaned_data.get('mobile_no', '')).lstrip('0')
        try:
            mobile_no = int(mobile_no)
        except ValueError:
            raise forms.ValidationError('Mobile number must be a valid integer.')

        return mobile_no
