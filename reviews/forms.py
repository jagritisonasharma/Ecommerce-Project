from django import forms
from .models import Product, Review

class CreateReviewForm(forms.Form):
    ratings = forms.IntegerField()
    headline = forms.CharField(max_length=100)
    review = forms.CharField()
    product = forms.ModelChoiceField(queryset=Product.objects.all())

class CreateReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('__all__')