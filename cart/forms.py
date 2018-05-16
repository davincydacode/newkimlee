from django.forms import ModelForm
from .models import products,productnew
from django import forms



class productForm(forms.Form):

	#image = forms.FileField(help_text="max. 40px")
	
	class Meta:
		model = products
		#fields = ['productname']

		fields = ('productname','price','category','datecreated','image')



class productnewForm(forms.ModelForm):

	
	
	class Meta:
		model = productnew
		#fields = ['productname']

		fields = ('productname','price','category','image','datecreated')


