from django.db import models
from django import forms

CATEGORIES = (
	('AER','Aerospace Engineering Sciences '),
	('APM','Applied Math' ),
	('CBE','Chemical & Biological Engineering'),
	('CEA','Civil, Environmental & Architectural Engineering '),
	('CSE','Computer Science'),
	('ECE','Electrical, Computer & Energy Engineering'),
	('Phy','Physics'),
	('EEn','Environmental Engineering'),
	('MEn','Mechanical Engineering'),
	('CSG','Colorado Space Grant'),
	('EnE','Engineering Education' ),
	('ATL','ATLAS'),
)

CHOICES=[('select1','select 1'),
         ('select2','select 2')]

class Contact(models.Model):

	Faculty_name = models.CharField(
	max_length=255,
	)
	Faculty_phone_number = models.CharField(
	max_length=255,

	) 
	Faculty_email = models.EmailField()

	Faculty_department_or_program    = models.CharField(max_length=12, choices=CATEGORIES)

	like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

	def __str__(self):
		return ' '.join([
		    self.Faculty_name,
		    self.Faculty_phone_number,
		    self.Faculty_email,
		    self.Faculty_department_or_program,
		])
	def get_absolute_url(self):

		return reverse('contacts-view', kwargs={'pk': self.id})

