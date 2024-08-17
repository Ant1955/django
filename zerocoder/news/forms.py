from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['title', 'news_user', 'short_description', 'text', 'pub_date']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'news_user': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор новости'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
			'pub_date': DateTimePickerInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
		}
