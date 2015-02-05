from django import forms


class CountTextForm(forms.Form):
    """
    The HTML form used to count input text.
    """
    text = forms.CharField(widget=forms.Textarea, max_length=100)
