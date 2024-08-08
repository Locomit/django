from django.shortcuts import render, redirect,HttpResponse
from .models import Emp, EmpForm, Account,AccountForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm()
        context={'form':f}
        return render(request,'addemp.html',context)
    
def add_account(request):
    if request.method=='POST':
        f=AccountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=AccountForm()
        context={'form':f}
        return render(request,'addaccount.html',context)

def emp_list(request):
    emp1=Emp.objects.all()
    context={'elist':emp1}
    return render(request,'emplist.html',context)

def delete1_emp(request,eid):
    eid=request.GET.get('id')
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/elist')

def delete2_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/elist')

def edit_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    if request.method=='POST':
        f=EmpForm(request.POST,instance=emp)
        f.save()
        return redirect('/elist')
    else:
        f=EmpForm(instance=emp)
        context={'form':f}
        return render(request,'addemp.html',context)

