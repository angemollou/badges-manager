from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from badge.models.task import Task
from badge.models.user import BadgeUser


def index(request):
    current_badge_user = BadgeUser.objects.get(user=request.user)
    current_user_tasks = Task.objects.filter(assignee=current_badge_user).order_by(
        "created_at"
    )
    print(current_user_tasks)
    context = {
        "current_user_tasks": current_user_tasks,
    }
    return render(request, "badge/index.html", context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "badge/task.html", {"task": task})


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    try:
        # is_completed = request.POST["is_completed"]
        task.is_completed = not task.is_completed
    except Exception as e:
        return render(
            request,
            "badge/task.html",
            {"task": task, "error_message": "Something went wrong!"},
        )
    else:
        task.save()
        return HttpResponseRedirect(reverse("task_detail", args=(task.id,)))
