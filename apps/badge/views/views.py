from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from badge.models.task import Task
from badge.models.user import BadgeUser


def get_current_user_data(user):
    badge_user = BadgeUser.objects.get(user=user)
    badge_model3ds = map(lambda a: a.badge.icon, badge_user.assertions.all())
    return {"badge_user": badge_user, "badge_model3ds": badge_model3ds}


@login_required(login_url="admin:login")
def index(request):
    current_badge_user = BadgeUser.objects.get(user=request.user)
    current_user_tasks = Task.objects.filter(assignee=current_badge_user).order_by(
        "created_at"
    )
    context = {
        "current_user_tasks": current_user_tasks,
        **get_current_user_data(request.user),
    }
    return render(request, "badge/index.html", context)


@login_required(login_url="admin:login")
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(
        request,
        "badge/task.html",
        {"task": task, **get_current_user_data(request.user)},
    )


@login_required(login_url="admin:login")
def complete_task(request, task_id):
    if not request.user.is_authenticated:
        return redirect("/admin")

    task = get_object_or_404(Task, pk=task_id)
    try:
        task.is_completed = not (task.is_completed or False)
        badge_user = BadgeUser.objects.get(user=request.user.id)
        points = task.points if task.is_completed else -task.points
        badge_user.set_new_score(points)
        task.save()
        return redirect(reverse("task_detail", args=(task.id,)))
    except Exception as e:
        print("Error: ", e)
        return render(
            request,
            "badge/task.html",
            {"task": task, "error_message": "Something went wrong!"},
        )
