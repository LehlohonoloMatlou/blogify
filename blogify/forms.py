from django import forms

from .models import Audience

class AudienceForm(forms.Form):
	name = forms.CharField(max_length = 35)
	description = forms.CharField(max_length = 150,widget = forms.Textarea)

class ArticleForm(forms.Form):
	title = forms.CharField(max_length = 35)
	context_image = forms.ImageField(required = False)
	description = forms.CharField(max_length=150, required = False)
	body = forms.CharField(widget=forms.Textarea( attrs={'data-toggle':'summernote'}))
	active = forms.BooleanField(required = False)
	audience = forms.ModelChoiceField(queryset= Audience.objects.all(),required= False,widget=forms.Select(attrs={'class':'size1'}))