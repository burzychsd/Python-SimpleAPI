from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
	title		= forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Title' }))
	description = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Short Description' }))
	content		= forms.CharField(label='', widget=forms.Textarea(attrs={ 'placeholder': 'Content...' }))
	author		= forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Author Name' }))

	class Meta:
		model = Article
		fields = [
			'title',
			'description',
			'content',
			'author'
		]