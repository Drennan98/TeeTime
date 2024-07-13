from django import forms
from .models import GolfCourse


class GolfCourseForm(forms.ModelForm):
    class Meta:
        model = GolfCourse
        fields = ["name", "location", "par", "holes"]
