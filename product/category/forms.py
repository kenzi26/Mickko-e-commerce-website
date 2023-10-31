from django import forms
class CategoryForm(forms.ModelForm):
    is_prime = forms.BooleanField( initial=True, required=False)

class SubCategoryForm(forms.ModelForm):
    is_prime = forms.BooleanField(initial=False, required=False)