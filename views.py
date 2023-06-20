from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == 'POST':
        Dob = int(request.POST['dob'])
        student = Student.objects.get(dob=Dob)
        physics = student.physics
        chemistry= student.chemistry
        maths = student.maths
        computer_science = student.computer_science
        total = physics+chemistry+maths+computer_science
        percent = total/400*100
        if(percent<33):
            status = 'Fail'
        else:
            status = 'Pass'
        params = {
            'dob': 'Dob',
            'name': student.name,
            'physics': physics,
            'chemistry': chemistry,
            'maths': maths,
            'computer_science': computer_science,
            'total': total,
            'percent': percent,
            'status': status
        }
        # print('get method', student.name)
        return render(request, 'result.html', params)
    else:
        print('get method')
    return render(request, 'result.html')



def admin_login(request):
    if 'user' in request.session:
        return render(request, 'adminpanel.html')
    else:
        return render(request, 'adminlogin.html')



def admin_panel(request):
    if 'user' in request.session:
        students = Student.objects.all()
        params = {'students': students}
        return render(request, 'admin_panel.html',params)
    else:
        if request.method == 'POST':
            user_name = request.POST['uname']
            pass_word = request.POST['pwd']
            if user_name == 'ADMIN' and pass_word == 'admin6797':
                request.session['user'] = user_name
                students = Student.objects.all()
                params = {'students': students}
                return render(request, 'adminpanel.html', params)
            else:
                return render(request, 'adminlogin.html')
        else:
            return render(request, 'adminlogin.html')


def delete_student(request, id):
    get_stu = Student.objects.get(id=id)
    get_stu.delete()
    return redirect('/adminpanel')


def edit_student(request, id):
    get_stu = Student.objects.get(id=id)
    params = {'student': get_stu}
    return render(request, 'edit.html', params)


def edit_confirm(request, id):
    if request.method == 'POST':
        get_stu = Student.objects.get(id=id)
        get_stu.name = request.POST['sname']
        get_stu.dob = request.POST['dob']
        get_stu.physics= request.POST['physics']
        get_stu.chemistry = request.POST['chemistry']
        get_stu.maths = request.POST['maths']
        get_stu.computer_science = request.POST['computer_science']
        total = int(request.POST['physics'])+int(request.POST['chemistry'])+int(request.POST['maths'])+int(request.POST['computer_science'])
        get_stu.total = total
        get_stu.percent = total/4 # type: ignore
        get_stu.save()
        return redirect('/adminpanel')
    else:
        return redirect('/adminlogin')

def admin_logout(request):
    del request.session['user']
    return redirect('/')



def add_student(request):
    return render(request, 'add_student.html')


def add_confirm(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        dob = request.POST['dob']
        physics = int(request.POST['physics'])
        chemistry = int(request.POST['chemistry'])
        maths = int(request.POST['maths'])
        computer_science = int(request.POST['computer_science'])
        total = physics+chemistry+maths+computer_science
        percent = total/400*100
        add_student = Student.objects.create(name=sname,dob=dob,
                        physics=physics,chemistry=chemistry,maths=maths,computer_science=computer_science,
                        total=total,perecent=percent)
        add_student.save()
        return redirect('/adminpanel')
    else:
        return redirect('/adminpanel')