from django.shortcuts import render, get_object_or_404

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
