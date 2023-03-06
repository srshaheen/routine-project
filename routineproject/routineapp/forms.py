from django import forms

from .models import Routine


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = "__all__"