from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello this is my first django project")

def name(request,s,r):
    return HttpResponse("<h1>Hello {} <br> rollno is {}</h1>".format(s,r))

def rollno(request,r):
    return HttpResponse("hello {}".format(r))

def home(request):
    return render(request,"FirstApp/index.html")

def maths_table(request,val):
   # data={}
    #for i in range(1,11):
     #  data[i]=i*val
   
    #return render(request,'FirstApp/maths_table.html',{'data':data,'val':val})

    data_list = []
    for i in range(1,11):
        data_list.append(i*val)
    return render(request,'FirstApp/maths_table.html',{'data_list':data_list,'val':val})

def login(request):
    static_name ='admin'
    static_pswd = 'neekenduku'
    if request.method == 'POST':
       user_name = request.POST.get('name')
       pswd = request.POST.get("password")
       if user_name==static_name and pswd == static_pswd :
            return HttpResponse("user logged in successfully")
       return HttpResponse("Invalid details")
       
    return render(request,'FirstApp/login.html')