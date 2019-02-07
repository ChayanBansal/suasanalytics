from django import forms
import mysql.connector

from django.db import connections
cursor = connections['studentanalytics'].cursor()
# hardcoding PG courses
# Refer Lookup table
get_pg_group="SELECT Title_ID FROM lookup_table WHERE title='M.B.A.'"
cursor.execute(get_pg_group)
pg_courses=[x for x in cursor.fetchall()]
data = [tuple(str(x) for x in pg_courses[0])]
get_courses_ug="SELECT `course_master`.`CM_Course_Name`,`course_master`.`CM_Course_ID` FROM `course_master` WHERE CM_Course_GroupID NOT IN ("+','.join(data[0]) +")"
cursor.execute(get_courses_ug)
courses_list=[ ( str(y),str(x) ) for x,y in cursor.fetchall()]

#

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
