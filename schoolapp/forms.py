from django import forms
from .models import Department, Course, Material

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2022)))
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    phone_number = forms.CharField(max_length=10)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.none())  # Empty at first
    purpose = forms.ChoiceField(choices=[('Enquiry', 'Enquiry'), ('Order', 'Order'), ('Return', 'Return')])
    materials = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Material.objects.all())
