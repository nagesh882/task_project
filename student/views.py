from django.shortcuts import render, redirect
from student.models import StudentInfo
from student.forms import StudentForm

# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        student = StudentInfo.objects.all()
        context = {
            'studentData':student
        }
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return redirect('sign_in')
    



def add_student(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = StudentForm()

        context = {
            "StudentAddForm":form    
        }
        return render(request, 'dashboard/add_student.html', context)
    else:
        return redirect('sign_in')
    



def edit_student(request, student_id):
    if request.user.is_authenticated:
        student = StudentInfo.objects.get(student_id=student_id)
        if request.method == "POST":
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = StudentForm(instance=student)
        
        context = {
            'StudentEditForm':form,
            'student_id': student_id
        }
            
        return render(request, 'dashboard/edit_student.html', context)
                
    else:
        return redirect('sign_in')
    


def delete_student(request, student_id):
    if request.user.is_authenticated:
        student = StudentInfo.objects.get(student_id=student_id)
        if student:
            student.delete()
            return redirect("dashboard")
                
    else:
        return redirect('sign_in')
        

def home(request):

    if request.user.is_authenticated:
        return render(request, 'dashboard/home.html')
                    
    else:
        return redirect('sign_in')