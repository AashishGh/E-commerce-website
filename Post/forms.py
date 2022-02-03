from django import forms
from .models import Product


class PostForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = [
            "Title",
            "category",
            "Name",
            "Address",
            "contact_number",
            "image1",
            "selling_price",
            "GoogleMap_Location",
            "description",
            "return_policy",
   
        ]
