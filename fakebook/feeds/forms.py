from django.forms import ModelForm
from .models import Feed


class FeedForm(ModelForm):
    class Meta:
        model = Feed
        fields = ['title', 'description', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'rows': '4'})
