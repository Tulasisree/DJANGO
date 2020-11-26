from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def register(req):
    if req.method == 'POST':
        fname = req.POST.get('fname')
        lname = req.POST.get('lname')
        roll = req.POST.get('roll')
        branch = req.POST.get('branch')
        email = req.POST.get('email')
        mobile = req.POST.get('phone')

        obj = Student_Register(First_name = fname,Last_name=lname,Roll_no=roll,Branch=branch,Email=email,Phone=mobile)
        obj.save()
        messages.success(req,"Student Registration successful")
        return redirect('student_data')
    return render(req,'Student/register.html')

def show(request):
    data = Student_Register.objects.all()
    return render(request,'Student/data.html',{'data':data})

def update(request,num):
    obj = Student_Register.objects.get(id=num)
    if request.method == 'POST':
        obj.First_name = request.POST.get('fname')
        obj.Last_name = request.POST.get('lname')
        obj.Roll_no = request.POST.get('roll')
        obj.Branch = request.POST.get('branch')
        obj.Email = request.POST.get('email')
        obj.Phone = request.POST.get('phone')
        obj.save()
        messages.success(request,"Student Details Edited")
        return redirect('student_data')

    return render(request,'Student/update_student.html',{'data':obj})

def delete(request,num):
    obj = Student_Register.objects.get(id=num)
    obj.delete()
    return redirect('student_data')

def  add_book(request):
    form = LibraryForm()
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
         form.save()
         return HttpResponse("Saved")
        return HttpResponse("Invalid Data")
    return render(request,'Student/add_book.html',{'form':form})

def edit_book(request,id):
    data=Library.objects.get(id=id)
    form = LibraryForm(request.POST or None,instance=data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("book details edited")
        return HttpResponse("INvalid data")
    return render(request,'Student/edit_book.html',{'form':form,'id':id})

def books(request):
    books = Library.objects.values("Department").distinct()
    return render(request,'Student/books.html',{'books':books})

def details(request,branch):
    data = Library.objects.filter(Department=branch)
    return render(request,'Student/details.html',{'data':data,'branch':branch})
    