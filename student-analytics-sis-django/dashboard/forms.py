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
    course      = forms.ChoiceField(choices=courses_list)
    enroll_year = forms.ChoiceField(choices=[]) 
    section     = forms.ChoiceField(choices=[]) 
    course.widget.attrs.update({'onChange': 'getEnrollYear(this.value)'})
    enroll_year.widget.attrs.update({'onChange': 'getSection(this.value)'})
