from django.db import models

class Instructor(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	honorary_title = models.CharField(max_length=50, null=True, blank=True)
	suffix = models.CharField(max_length=50, null=True, blank=True)
	batch = models.CharField(max_length=50)
	undergrad_course = models.CharField(max_length=100)
	undergrad_school = models.CharField(max_length=100)
	undergrad_award = models.CharField(max_length=100)
	undergrad_scholarship = models.CharField(max_length=100)
	postgrad_course = models.CharField(max_length=100)
	postgrad_school = models.CharField(max_length=100)
	postgrad_award = models.CharField(max_length=100)
	postgrad_scholarship = models.CharField(max_length=100)
	other_achievments = models.CharField(max_length=100)
	status = models.CharField(max_length=50)
	email = models.CharField(max_length=100, null=True, blank=True)
	profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
	

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")