from django.shortcuts import render,redirect
from .form import Inputform
def Indexpage(request):
    if request.method=='POST':
        form=Inputform(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form=Inputform()
        return render(request,'index.html',{'form':form})

