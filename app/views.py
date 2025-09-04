from django.shortcuts import render

def task_view(request):
    title = request.GET.get("title", "Django Task1")
    message = request.GET.get("message", "This is a dynamically rendered HTML page!")
    tasks_param = request.GET.get("tasks")
    if tasks_param:
        tasks = [task.strip() for task in tasks_param.split(",") if task.strip()]
    else:
        tasks = ["Learn Django", "Create Views", "Connect URLs", "Style with CSS"]

    context = {
        "title": title,
        "message": message,
        "tasks": tasks
    }
    return render(request, 'task.html', context)