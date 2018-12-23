from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import CorrForm, getEnrollYearForm, getSectionForm
import pandas as pd

# Create your views here.
import mysql.connector
mydb = mysql.connector.connect(
  host="117.232.120.165",
  user="root",
  passwd="suas@1234",
  database="studentanalytics"
)
mycursor = mydb.cursor()

def index_view(request):
    return render(request, 'index.html', {})

@login_required
def home_view(request):

	if request.method=="POST": 	#Obtaining selected value of corelation options
		correl_type=int(request.POST['correl_type'])
		
		if correl_type==1:
			return redirect('dashboard:corr_view3') #Use namespace : to resolve URL name!!
	
	context={}
	return render(request, 'dashboard/home.html', context)

@login_required
def corr_view3(request):
    my_form = CorrForm()
    return render(request,'dashboard/corr_view3.html',{'form': my_form})

@login_required
def corr_view3_getEnrollYear(request):
    if request.method=="POST":
        my_form = getEnrollYearForm(request.POST, files=request.FILES)
        if my_form.is_valid():
            my_form = my_form.cleaned_data
            course = my_form['course']
            all="All"
            if course == all :
                get_year="SELECT DISTINCT substr(created_date,1,4), substr(created_date,1,4) FROM `student_master` student"
            else:
                get_year="SELECT DISTINCT substr(created_date,1,4), substr(created_date,1,4) FROM `student_master` student WHERE Course_ID ='"+str(course)+"'"
            mycursor = mydb.cursor()
            mycursor.execute(get_year)
            years=dict(mycursor.fetchall())
            return JsonResponse(years)

@login_required
def corr_view3_getSection(request):
    if request.method=="POST":
        course      = request.POST["course"]
        enroll_year = request.POST["enroll_year"]

        all="All"
        if (course !=all) & (enroll_year !=all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE Course_ID="+course+" AND substr(created_date,1,4)="+enroll_year
        elif (course !=all) & (enroll_year ==all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE Course_ID="+course
        elif (course ==all) & (enroll_year !=all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE substr(created_date,1,4)="+enroll_year
        else:
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master"
        mycursor = mydb.cursor()
        mycursor.execute(get_section)
        sections=dict(mycursor.fetchall())
        return JsonResponse(sections)

@login_required
def corr_view3_updateVisualization(request):
    if request.method == "POST":
        course      = request.POST["course"]
        enroll_year = request.POST["enroll_year"]
        section     = request.POST["section"]
        all="All"
        query=""
        if( (section != "All") & (enroll_year !="All") & (course != "All")):
            query=str("SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID ="+course+" AND substr(sm.created_date,1,4)="+enroll_year+" AND sm.Division='"+section+"'")
        elif ( (section ==all) & (enroll_year !=all ) & (course !=all)):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID ="+course+" AND substr(sm.created_date,1,4)="+enroll_year
        elif( (section ==all ) & (enroll_year ==all ) & (course !=all)):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID ="+course
        elif( (section ==all ) & (enroll_year ==all ) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID"
        elif( (section !=all) & (enroll_year ==all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Division='"+section+"'"
        elif( (section !=all) & (enroll_year !=all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND substr(sm.created_date,1,4)="+enroll_year+" AND sm.Division='"+section+"'"
        elif( (section ==all ) & (enroll_year !=all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND substr(sm.created_date,1,4)="+enroll_year
        else:
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID ="+course+" AND sm.Division='"+section+"'"
        mycursor=mydb.cursor()
        mycursor.execute(query)
        result=mycursor.fetchall() 
        df=pd.DataFrame(result,columns=['result','sgpa','cgpa','exam_name', 'percentage','classgrade','course_id'])
        df=df[(df["exam_name"]=="HSC / 12th or Equivalent") | (df["exam_name"]=="HSC / 12th (Sci); or Equivalent")]
        dataSet = {
            #data  df.loc[:,["percentage", "sgpa"]].set_index["x","y"].to_dict('records')
        }
        #data = df.loc[:,["percentage", "sgpa"]].set_index["x","y"].to_dict('records')
        df=df.loc[:,["percentage", "sgpa"]]
        df.columns=["x","y"]
        df=df.astype(float)
        data=df.to_dict('records')
        return JsonResponse({"data":data,"corr":df.corr().loc["x","y"]})
