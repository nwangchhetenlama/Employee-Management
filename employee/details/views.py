from django.shortcuts import render,redirect
from .models import employee
# Create your views here.
from .forms import employeeform

def base(request):

    return render(request,'base.html')


def create(request):
    formm=employeeform()
    
    if request.method=='POST':
        formm=employeeform(request.POST)
        if formm.is_valid():
            formm.save()
            return redirect("/")


    context={'formm':formm}
    return render(request,'create.html',context)


def listt(request):

    lists=employee.objects.all()
    context={"lists":lists}


    return render(request,'list.html',context)

def update(request,pk):
    formm=employee.objects.get(id=pk)
    form_up=employeeform(instance=formm)
    if request.method=='POST':
        form_up=employeeform(request.POST,instance=formm)
        if form_up.is_valid():
            form_up.save()
            return redirect('/list')
    

    context={'form_up':form_up}
    return render(request,'update.html',context)


def deletee(request,pk):
    form_d=employee.objects.get(id=pk)
    if request.method=='POST':
        form_d.delete()
        return redirect('/list')

    context={'employee':form_d}

    return render(request,'delete.html',context)
