from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["text", "author", "weight"]
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }