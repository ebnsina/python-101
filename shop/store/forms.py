from django.forms import ModelForm
from .models import Shipping


class ShippingForm(ModelForm):
    class Meta:
        model = Shipping
        fields = ['city', 'postcode', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})