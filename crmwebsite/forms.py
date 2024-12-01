from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Instructor

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class AddInstructorForm(forms.ModelForm):

    first_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), 
        label="First Name"
    )
    middle_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"Middle Name", "class":"form-control"}), 
        label="Middle Name"
    )
    last_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), 
        label="Last Name"
    )
    honorary_title = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. Atty.", "class":"form-control"}), 
        label="Honorary Title"
    )
    suffix = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. Jr., RL", "class":"form-control"}), 
        label="Suffix"
    )
    
    batch = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"FCEER Batch #", "class":"form-control"}), 
        label="FCEER Batch"
    )
    email = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), 
        label="Email"
    )
    undergrad_course = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. B Library and Information Science", "class":"form-control"}), 
        label="Undergraduate Course"
    )
    undergrad_school = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. University of The Philippines - Diliman, School of Library and Information Sciences", "class":"form-control"}), 
        label="Undergraduate School"
    )
    undergrad_award = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. Summa Cum Laude", "class":"form-control"}), 
        label="Undergraduate Award"
    )
    undergrad_scholarship = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. DOST Undergraduate Scholarship Program", "class":"form-control"}), 
        label="Undergraduate Scholarship"
    )
    postgrad_course = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. Juris Doctor", "class":"form-control"}), 
        label="Postgraduate Course"
    )
    postgrad_school = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. University of The Philippines - Diliman, College of Law", "class":"form-control"}), 
        label="Postgraduate School"
    )
    postgrad_award = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. Summa Cum Laude", "class":"form-control"}), 
        label="Postgraduate Award"
    )
    postgrad_scholarship = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"e.g. UP College of Law Scholarship Program", "class":"form-control"}), 
        label="Postgraduate Scholarship"
    )

    other_achievments = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder":"List of Achievments", "class":"form-control"}), 
        label="Other Achievments"

    )
    profile_image = forms.ImageField(
        required=False, 
        widget=forms.widgets.FileInput(attrs={"class":"form-control"}), 
        label="Profile Image"
    )
    status = forms.ChoiceField(
        required=True,
        choices=[('active', 'Active'), ('inactive', 'Inactive')],
        widget=forms.widgets.Select(attrs={"class":"form-control"}),
        label="Status"
    )

    class Meta:
        model = Instructor
        exclude = ("user", "updated_by", "last_updated",)