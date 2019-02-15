from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import CorrForm, getEnrollYearForm, getSectionForm
import pandas as pd



from django.db import connections
cursor = connections['studentanalytics'].cursor()

# Getting PG Courses
get_pg_group="SELECT Title_ID FROM lookup_table WHERE title='M.B.A.'"
cursor.execute(get_pg_group)
pg_courses=[x for x in cursor.fetchall()]
data_pg = [tuple(str(x) for x in pg_courses[0])]

# Getting UG Courses
get_ug_group="SELECT Title_ID FROM lookup_table WHERE title IN ('B.Tech', 'B.B.A.')"
cursor.execute(get_ug_group)
ug_courses=[x for x in cursor.fetchall()]
data_ug = [tuple(str(x) for x in ug_courses[0])]

# Index page
def index_view(request):
    return render(request, 'index.html', {})

# dashboard Options page
@login_required
def home_view(request):

	if request.method=="POST": 	#Obtaining selected value of corelation options
		correl_type=int(request.POST['correl_type'])
		
		if correl_type==3:
			return redirect('dashboard:corr_view3') #Use namespace : to resolve URL name!!
		elif correl_type==2:
			return redirect('dashboard:corr_view2') #Use namespace : to resolve URL name!!
	
	context={}
	return render(request, 'dashboard/home.html', context)

# UG percentage vs. SGPA page
@login_required
def corr_view3(request):
    my_form = CorrForm()
    my_form.setCourse("UG")
    return render(request,'dashboard/corr_view3.html',{'form': my_form})

# PG percentage vs. SGPA page
@login_required
def corr_view2(request):
    my_form = CorrForm()
    my_form.setCourse("PG")
    return render(request,'dashboard/corr_view2.html',{'form': my_form})

# AJAX request
@login_required
def corr_view2_getEnrollYear(request): #PG
    if request.method=="POST":
        my_form = getEnrollYearForm(request.POST, files=request.FILES)
        course = request.POST["course"]
        all="All"
        if course == all :
            get_year="SELECT DISTINCT substr(created_date,1,4), substr(created_date,1,4) FROM `student_master` student WHERE Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_pg[0]) +")"+")"
            
        else:
            get_year="SELECT DISTINCT substr(created_date,1,4), substr(created_date,1,4) FROM `student_master` student WHERE Course_ID ='"+str(course)+"'"
        cursor = connections['studentanalytics'].cursor()
        cursor.execute(get_year)
        years=dict(cursor.fetchall())
        return JsonResponse(years)

# AJAX request
@login_required
def corr_view3_getSection(request): #UG
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
        cursor = connections['studentanalytics'].cursor()
        cursor.execute(get_section)
        sections=dict(cursor.fetchall())
        return JsonResponse(sections)

# AJAX request
@login_required
def corr_view3_getEnrollYear(request): #UG
    if request.method=="POST":
        my_form = getEnrollYearForm(request.POST, files=request.FILES)
        course = request.POST["course"]
        all="All"
        if course == all :
            get_year="SELECT DISTINCT substr(created_date,1,4), substr(created_date,1,4) FROM `student_master` student  WHERE Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_ug[0]) +")"+")"
        else:
            get_year="SELECT DISTINCT substr(created_date,1,4), substr(created_date,1,4) FROM `student_master` student WHERE Course_ID ='"+str(course)+"'"
        cursor = connections['studentanalytics'].cursor()
        cursor.execute(get_year)
        years=dict(cursor.fetchall())
        return JsonResponse(years)

# AJAX request
@login_required
def corr_view2_getSection(request): #PG
    if request.method=="POST":
        course      = request.POST["course"]
        enroll_year = request.POST["enroll_year"]

        all="All"
        if (course !=all) & (enroll_year !=all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE Course_ID="+course+" AND substr(created_date,1,4)="+enroll_year
        elif (course !=all) & (enroll_year ==all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE Course_ID="+course
        elif (course ==all) & (enroll_year !=all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE substr(created_date,1,4)="+enroll_year + " WHERE Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_pg[0]) +")"+")"
        else:
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master  WHERE Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_pg[0]) +")"+")"
        cursor = connections['studentanalytics'].cursor()
        cursor.execute(get_section)
        sections=dict(cursor.fetchall())
        return JsonResponse(sections)

# AJAX request
@login_required
def corr_view3_getSection(request): #UG
    if request.method=="POST":
        course      = request.POST["course"]
        enroll_year = request.POST["enroll_year"]

        all="All"
        if (course !=all) & (enroll_year !=all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE Course_ID="+course+" AND substr(created_date,1,4)="+enroll_year
        elif (course !=all) & (enroll_year ==all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE Course_ID="+course
        elif (course ==all) & (enroll_year !=all):
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master WHERE substr(created_date,1,4)="+enroll_year + " WHERE Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_ug[0]) +")"+")"
        else:
            get_section="SELECT DISTINCT Division, DIVISION FROM student_master  WHERE Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_ug[0]) +")"+")"
        cursor = connections['studentanalytics'].cursor()
        cursor.execute(get_section)
        sections=dict(cursor.fetchall())
        return JsonResponse(sections)

# AJAX request
@login_required
def corr_view3_updateVisualization(request):
    if request.method == "POST":
        cursor = connections['studentanalytics'].cursor()
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
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_ug[0]) +")"+")"
        elif( (section !=all) & (enroll_year ==all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Division='"+section+"' AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_ug[0]) +")"+")"
        elif( (section !=all) & (enroll_year !=all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND substr(sm.created_date,1,4)="+enroll_year+" AND sm.Division='"+section+"' AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_ug[0]) +")"+")"
        elif( (section ==all ) & (enroll_year !=all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND substr(sm.created_date,1,4)="+enroll_year + " AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_ug[0]) +")"+")"
        else:
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID ="+course+" AND sm.Division='"+section+"'"
        cursor.execute(query)
        result=cursor.fetchall()
        
        result=list(result)
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
    
# AJAX request
@login_required
def corr_view2_updateVisualization(request):
    if request.method == "POST":
        cursor = connections['studentanalytics'].cursor()
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
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_pg[0]) +")"+")"
        elif( (section !=all) & (enroll_year ==all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Division='"+section+"' AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_pg[0]) +")"+")"
        elif( (section !=all) & (enroll_year !=all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND substr(sm.created_date,1,4)="+enroll_year+" AND sm.Division='"+section+"' AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_pg[0]) +")"+")"
        elif( (section ==all ) & (enroll_year !=all) & (course ==all )):
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND substr(sm.created_date,1,4)="+enroll_year + " AND sm.Course_ID IN (SELECT CM_Course_ID FROM course_master WHERE CM_Course_GroupID IN ("+','.join(data_pg[0]) +")"+")"
        else:
            query="SELECT srm.result, srm.SGPA, srm.CGPA, student.ExamName,student.percentage, student.ClassGrade,sm.Course_ID FROM srm_gradecard_issued srm, student_academic_details student, student_master sm WHERE sm.student_ID=srm.StudentID AND sm.student_ID=student.Student_ID AND srm.StudentID=student.Student_ID AND sm.Course_ID ="+course+" AND sm.Division='"+section+"'"
        cursor.execute(query)
        result=cursor.fetchall()
        result=list(result)
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
