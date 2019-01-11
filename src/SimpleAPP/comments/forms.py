from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
	author	= forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Your Name' }))
	text	= forms.CharField(label='', widget=forms.Textarea(attrs={ 'placeholder': 'Comment...' }))
	class Meta:
		model = Comment
		fields = [
			'author',
			'text'
		]
	# def clean_author(self, *args, **kwargs):
	# 	author = self.cleaned_data.get('author')
	# 	if not 'CFE' in author:
	# 		raise forms.ValidationError('This is not the valid author')
	# 	return author
			

class RawCommentForm(forms.Form):
	author	= forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Your Name' }))
	text	= forms.CharField(label='', widget=forms.Textarea(attrs={ 'placeholder': 'Comment...' }))