from django import forms
cities=(('Ind','Indore'),
        ('dws','Dewas'),
        ('bhl','Bhopal'),
        ('ujn','Ujjain'))
class Inputform(forms.Form):
    fname=forms.CharField(label="First Name",max_length=20)
    lname=forms.CharField(label="Last Name",max_length=20)
    rno=forms.IntegerField(label="Roll Number",help_text="Enter 8 Digit Rollno")
    password=forms.CharField(label="Password",max_length=10,widget=forms.PasswordInput())
    email=forms.EmailField(label="Email")
    comment=forms.CharField(label="Message",help_text="Enter you message",widget=forms.Textarea())
    city=forms.ChoiceField(choices=cities)
    date=forms.DateField(label="Date of Admission")
    resume=forms.MultipleChoiceField(choices=cities)
    website=forms.URLField()