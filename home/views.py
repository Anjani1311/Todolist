from django.shortcuts import render,redirect,HttpResponseRedirect
from home.models import Task


# Create your views here.
def index(request):
    context={"success":False,"name":"Anjani"}
    if request.method =='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        ins=Task(task_title=title,task_description=desc)
        ins.save()
        context={"success":True}
    return render(request,'index.html',context)


def about(request):
    allTasks=Task.objects.all()
    """ print(allTasks)
    for item in allTasks:
        print(item.task_title) """
    for item in allTasks:
        print(item.task_title)
    context={"tasks":allTasks}
    return render(request,'about.html',context)

def delete_data(request,id):
    if request.method =='POST':
        target_data=Task.objects.get(pk=id)
        target_data.delete()
        return HttpResponseRedirect('/about')

def edit_data(request,id):
    if request.method =='POST':
        target_data=Task.objects.get(pk=id)

        title=request.POST['title']
        desc=request.POST['desc']
        ins=Task(task_title=title,task_description=desc)
        ins.save()
        return HttpResponseRedirect('/about')

    return render(request,'update.html')
