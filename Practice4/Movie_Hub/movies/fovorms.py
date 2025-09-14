from django import forms

class GenreForm(forms.ModelForm):

	name = forms.CharField(max_length=100)
	description = forms.TextField(blank=True, null=True)


