from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(empty_value='sky',error_messages={'required':'enter valid'})
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    roll=forms.IntegerField()
    website=forms.URLField(min_length=5,max_length=50)
    description=forms.CharField(widget=forms.Textarea)
    feedback=forms.CharField(min_length=5,max_length=50)
    chack=forms.BooleanField(label='I agree')
    # email=forms.EmailField()
    # mobile=forms.IntegerField()
    # key=forms.CharField(widget=(forms.HiddenInput))
    # form_name=forms.CharField()