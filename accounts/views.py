from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *
from .filters import *
from .decorators import *

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # signal runs here

            messages.success(request, 'Account was successfully created for ' + username + '. Kindly login and fill in the required information in "Update Profile" before placing any orders')

            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/AUTH/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/AUTH/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    students = Student.objects.all()
    orders = Order.objects.all().order_by('-date_created')

    pending = orders.filter(status='Pending').count()
    processing = orders.filter(status='Processing').count()
    done = orders.filter(status='Order Done').count()

    myOrderFilter = OrderFilter(request.GET, queryset=orders)
    orders = myOrderFilter.qs

    context = {'students':students, 'orders':orders, 'pending':pending, 'processing':processing, 'done':done, 'myOrderFilter':myOrderFilter}

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'RD'])
def workOrders(request):
    work_orders = WorkOrder.objects.all()

    context = {'work_orders':work_orders}
    return render(request, 'accounts/work-orders.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'RD'])
def allStudents(request):
    students = Student.objects.all().order_by('student_id')

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    context = {'students':students, 'myFilter':myFilter}
    return render(request, 'accounts/all_students.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'RD'])
def student(request, pk):
    student = Student.objects.get(id=pk)

    orders = student.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'student':student, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'accounts/student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentPage(request):

    orders = request.user.student.order_set.all().order_by('-date_created')
    # orders = Order.objects.filter(user=request.user)

    order_count = orders.count()

    pending = orders.filter(status='Pending').count()
    processing = orders.filter(status='Processing').count()
    done = orders.filter(status='Order Done').count()

    context = {'orders':orders, 'pending':pending, 'processing':processing, 'order_count':order_count, 'done':done}
    return render(request, 'accounts/student_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def accountSettings(request):
    student = request.user.student

    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['maintenance'])
def maintenance(request):

    students = Student.objects.all()
    orders = Order.objects.filter(status='Processing').order_by('-date_created')

    # pending = orders.filter(status='Pending').count()
    processing = orders.filter(status='Processing').count()
    # done = orders.filter(status='Order Done').count()

    myMaintenanceOrderFilter = MaintenanceOrderFilter(request.GET, queryset=orders)
    orders = myMaintenanceOrderFilter.qs

    context = {'students':students, 'orders':orders, 'processing':processing, 'myMaintenanceOrderFilter':myMaintenanceOrderFilter}

    return render(request, 'accounts/maintenance.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['RD', 'admin', 'student'])
def createOrder(request):

    # form = OrderForm()
    #
    # if request.method == 'GET':
    #
    #     context = {'form':form}
    #     return render(request, 'accounts/CRUD/order_form.html', context)
    # else:
    #     form = OrderForm(request.POST)
    #     neworder = form.save(commit=False)
    #     neworder.user = request.user
    #     neworder.save()
    #     return redirect('/')

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/CRUD/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['maintenance', 'RD', 'admin'])
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/CRUD/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['RD', 'admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/CRUD/delete.html', context)
