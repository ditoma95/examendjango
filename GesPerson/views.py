from django.shortcuts import render
from GesPerson.forms import TeacherForm, StudentForm
from django.shortcuts import render,  redirect
from django.db.models import Count


from GesPerson.models import Teacher, Student

def index(request):
   return render(request, "accueil/index.html")
# Create your views here.
def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("teachers/show_t")
            except:
                pass
    else:
        form = TeacherForm()
       
        return render(request, "teachers/add_teacher.html", {'form':form})
    
def show_t(request):
    recupteacher = Teacher.objects.all()
    nobreteacher = recupteacher.count()
    return render(request, 'teachers/show_t.html', {'recupteacher': recupteacher, 'nobreteacher' : nobreteacher})
    


def edit(request, id):
    teachers = Teacher.objects.get(id=id)
    return render(request, 'teachers/edit.html', {'teachers': teachers})


def update_teachers(request, id):
    teachers = teachers.objects.get(id=id)
    form = TeacherForm(request.POST, instance=teachers)
    if form.is_valid():
        form.save()
        return redirect('teachers/show_t')
    return render(request, 'teachers/update_teachers.html', {'teachers':teachers})



    
#---------------------------------etudiant-----------------------------------------


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("students/show_s")
            except:
                pass
    else:
        form = StudentForm()
       
        return render(request, "students/add_student.html", {'form':form})
    
def show_s(request):
    recupstudent = Student.objects.all()
    nobreetudiant = recupstudent.count()
    return render(request, 'students/show_s.html', {'recupstudent': recupstudent, 'nobreetudiant' : nobreetudiant})


def edit_s(request, id):
    students = Student.objects.get(id=id)
    return render(request, 'students/edit_s.html', {'students': students})


def update_students(request, id):
    students = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return redirect('students/show_t')
    return render(request, 'students/update_students.html', {'students':students})