#from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404 , render,redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, "index.html",{
        'title' : title
    })

def hello(request, username):
    # result = id + 100 * 2
    return HttpResponse("<h2>hello %s </h2>" % username)

def about(request):
    return HttpResponse('Dimelo')

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request , "projects.html", {
        "projects":projects
    })

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task , id = id)
    #task = get_object_or_404(Task , title = title)
    tasks = Task.objects.all()
    #return HttpResponse('task: %s' % task.title)
    return render(request,"tasks.html",{
        "tasks": tasks
    })

def create_task(request):
    
    if request.method == 'GET':
        return render(request,'create_task.html',{
            'form' : CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'], project_id=2)
        return redirect('/tasks/')

def create_project(request):
    if request.method == 'GET':
        return render(request,"create_project.html", {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
        # #return render(request,"create_project.html", {
        #     'form': CreateNewProject()
        # })