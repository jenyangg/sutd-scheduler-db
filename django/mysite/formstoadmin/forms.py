from django import forms
import datetime
from django_select2.forms import ModelSelect2Widget
from users.models import Module, Class
PREFERRED_TIMINGS = (
    ('morning', 'Morning'),
    ('earlyAfternoon', 'Early Afternoon'),
    ('lateAfternoon', 'Late Afternoon')
)

# useful form fields
'''
help_text=""
'''


class ScheduleRequestForm(forms.Form):
    name = forms.CharField(disabled=True)
    course_code = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20, 'placeholder': "Enter the course code this request is relevant to"}))

    class_related = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 2, 'cols': 20, 'placeholder': "Input relevant classes separated by a comma. Eg. CC1, CC2."}))
    preferred_timings = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PREFERRED_TIMINGS)
    reasons = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}))
    remarks = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}))


PILLARS = (
    ('asd', 'ASD'),
    ('epd', 'EPD'),
    ('esd', 'ESD'),
    ('istd', 'ISTD'),
    ('hass', 'HASS'),
)


class EventRequestForm(forms.Form):
    persons_in_charge = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20, 'placeholder': "Separate names by commas"}))
    event_name = forms.CharField()
    relevant_pillars = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PILLARS)
    start_date = forms.DateTimeField(input_formats=['%d/%m/%y'], help_text="DD/MM/YYYY")
    start_time = forms.DateTimeField(input_formats=['%H:%M'], help_text="HH:MM eg. 14:30")
    end_date = forms.DateTimeField(input_formats=['%d/%m/%y'], help_text="DD/MM/YYYY")
    end_time = forms.DateTimeField(input_formats=['%H:%M'], help_text="HH:MM eg. 16:30")
    duration = forms.DurationField()


LOCATION_TYPE = (
    ('LT', "Lecture Theatre"),
    ('Cohort', "Cohort classroom"),
)

CLASSES = (
    ('lab', "Lab"),
    ('cohort', "Cohort Class"),
    ('lecture', "Lecture"),
)

PILLARS = (
    ('asd', 'ASD'),
    ('epd', 'EPD'),
    ('esd', 'ESD'),
    ('istd', 'ISTD'),
    ('hass', 'HASS'),
)
# TODO: FOR RELEVANT FIELDS, SEARCH FROM DATABASE ONCE FIELDS ARE BEING FILLED


class inputModuleInformation(forms.Form):
    subject = forms.CharField(required=False, disabled=True)
    pillar = forms.ChoiceField(choices=PILLARS)
    subject_code = forms.CharField()
    term = forms.CharField()
    core = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'placeholder': "True/False"}))
    subject_lead = forms.CharField()
    cohort_size = forms.CharField()
    cohorts = forms.CharField()
    enrolment_size = forms.CharField()
    cohorts_per_week = forms.CharField()
    lectures_per_week = forms.CharField(required=False)
    labs_per_week = forms.CharField(required=False)


class inputClassInformation(forms.Form):
    module = forms.ModelChoiceField(queryset=Module.objects.all())
    title = forms.CharField(disabled=True, required=False)
    pillar = forms.CharField(disabled=True, required=False)
    Type = forms.CharField(disabled=True, required=False)
    class_related = forms.CharField(disabled=True, required=False)
    location = forms.CharField()
    duration = forms.CharField(disabled=True, required=False)
    start = forms.CharField(disabled=True, required=False)
    end = forms.CharField(disabled=True, required=False)
    description = forms.CharField()
    makeup = forms.CharField()
    assigned_professors = forms.CharField(help_text="Please separate professors\' names with a comma")
