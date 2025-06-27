from maths.models import Result
from django import forms
class ResultForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get('value')
        error = cleaned_data.get('error')

        if value and error:
            raise forms.ValidationError("Podaj tylko jedną z wartości")
        elif not (value or error):
            raise forms.ValidationError("Nie podano żadnej wartości!")

    class Meta:
        model = Result
        fields = ["value", "error"]