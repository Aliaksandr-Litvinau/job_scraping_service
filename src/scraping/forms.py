from django import forms

from scraping.models import City, ProgrammingLanguage


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name="slug", required=False
    )
    prog_lang = forms.ModelChoiceField(
        queryset=ProgrammingLanguage.objects.all(), to_field_name="slug",
        required=False
    )
