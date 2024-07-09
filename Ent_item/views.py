from django.shortcuts import render, redirect
from Ent_item.models import Student
from Ent_item.forms import StudentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    user = None
    error_message = None
    if request.POST:
        u_name = request.POST['username']
        p_word = request.POST['password']
        print(u_name, p_word)
        try:
            user = User.objects.create_user(username = u_name, password = p_word)
            return redirect('login')
        except Exception as e:
            error_message = str(e)
    return render(request, 'signup.html', {'user':user, 'error_message':error_message})

def login_view(request):
    error_message = None
    if request.POST:
        u_name = request.POST['username']
        p_word = request.POST['password']
        user_log = authenticate(username = u_name, password = p_word)
        if user_log:
            login(request, user_log)
            return redirect('home')
        else:
            error_message = "Invalid data!!!"
    return render(request, 'login.html', {'error_message':error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login/')
def sample(request):
    S_data = Student.objects.all()
    return render(request, "index.html", {'S_data': S_data})

@login_required(login_url='login/')
def create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same view or another view
    else:
        form = StudentForm()
    return render(request, 'create.html', {'form': form})

@login_required(login_url='login/')
def delete_view(request, id):
    form = Student.objects.get(id=id)
    form.delete()
    return redirect('home')

@login_required(login_url='login/')
def update_view(request, id):
    student = Student.objects.get(id = id)
    return render(request, "update.html", {'student': student})

@login_required(login_url='login/')
def update_recd(request, id):
    student = Student.objects.get(id = id)
    sname = request.POST['sname']
    sclass = request.POST['sclass']
    saddress = request.POST['saddress']
    student.s_name = sname
    student.s_class = sclass
    student.s_address = saddress
    print(student)
    student.save()
    return redirect('home')