from django import forms
import mysql.connector

from django.db import connections
cursor = connections['studentanalytics'].cursor()

get_courses="SELECT `course_master`.`CM_Course_Name`,`course_master`.`CM_Course_ID` FROM `studentanalytics`.`course_master`"
cursor.execute(get_courses)
courses_list=[ ( str(y),str(x) ) for x,y in cursor.fetchall()]

class CorrForm(forms.Form):
    course      = forms.ChoiceField(choices=courses_list+[('All','All')])
    enroll_year = forms.ChoiceField(choices=[]) 
    section     = forms.ChoiceField(choices=[]) 
    course.widget.attrs.update({'onChange': 'getEnrollYear(this.value)','class':'form-control'})
    enroll_year.widget.attrs.update({'onChange': 'getSection(this.value)','class':'form-control'})
    section.widget.attrs.update({'onChange': 'updateVisualization(this.value)','class':'form-control'})

class getEnrollYearForm(CorrForm):
    def __init__(self, *args, **kwargs):
        super(getEnrollYearForm, self).__init__(*args, **kwargs)
        del self.fields['enroll_year']
        del self.fields['section']

# class getSectionForm(CorrForm):
#     def __init__(self, *args, **kwargs):
#         super(getSectionForm, self).__init__(*args, **kwargs)
#         del self.fields['section']

class getSectionForm(CorrForm):
    course      = forms.ChoiceField(choices=[])
    enroll_year = forms.ChoiceField(choices=[]) 
