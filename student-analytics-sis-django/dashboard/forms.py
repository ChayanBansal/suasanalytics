from django import forms
import mysql.connector
mydb = mysql.connector.connect(
  host="117.232.120.165",
  user="root",
  passwd="suas@1234",
  database="studentanalytics"
)
mycursor = mydb.cursor()
get_courses="SELECT `course_master`.`CM_Course_Name`,`course_master`.`CM_Course_ID` FROM `studentanalytics`.`course_master`"
mycursor.execute(get_courses)
courses_list=[ ( str(y),str(x) ) for x,y in mycursor.fetchall()]

class CorrForm(forms.Form):
    course      = forms.ChoiceField(choices=courses_list+[('All','All')])
    enroll_year = forms.ChoiceField(choices=[]) 
    section     = forms.ChoiceField(choices=[]) 
    course.widget.attrs.update({'onChange': 'getEnrollYear(this.value)'})
    enroll_year.widget.attrs.update({'onChange': 'getSection(this.value)'})
    section.widget.attrs.update({'onChange': 'updateVisualization(this.value)'})

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

mydb.close()