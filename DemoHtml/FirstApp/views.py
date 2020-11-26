from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"FirstApp/home.html")

def table(request):
    return render(request,"FirstApp/table.html")

def forms(request):
    if request.method == 'POST':
       uname = request.POST['name']
       uemail = request.POST['email']
       udob = request.POST['dob']
       ubranch = request.POST['branch']
       ugender = request.POST['gender']
       return render(request,'FirstApp/data.html',{'name':uname,'email':uemail,'dob':udob,'branch':ubranch,'gender':ugender})
    
    return render(request,"FirstApp/forms.html")

def names(request,names):
    return render(request,'FirstApp/names.html',{'names':names})

def college(request):
    col="AUCEW"
    return render(request,'FirstApp/college.html',{'college':col})

def number(request,num):
    l=[]
    for i in range(1,num+1):
        l.append(i)
    return render(request,'FirstApp/number.html',{'num':l})

def login(request):
    if(request == POST):
        for i in l:
          l.append(request.POST['name'],request.POST['email'],request.POST['password'])

    return render(request,'FirstApp/login.html')