from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = '__all__'
		exclude = ['owner']
		labels = {'text': 'Topic',
				  'public': 'Public topic can be seen by all users'}


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
