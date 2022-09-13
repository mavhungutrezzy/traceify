import json
import os

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Application

CLEARBIT_API_KEY = os.environ.get("CLEARBIT_API_KEY")


def application(request):
    """Render application page with user's submitted applications"""
    applications = Application.objects.all()

    return render(
        request, "application/application.html", {"applications": applications}
    )


@login_required(login_url="login")
def create_application(request):
    """Get application details from user and create new application object"""
    if request.method != "POST":
        return render(request, "application/application.html")
    name = request.POST.get("name")
    title = request.POST.get("title")
    location = request.POST.get("location")
    notes = request.POST.get("notes")
    status = request.POST.get("status")
    date = request.POST.get("date")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CLEARBIT_API_KEY}",
    }

    url = "https://company.clearbit.com/v1/domains/find?name=query"
    response = requests.get(url.replace("query", name), headers=headers)
    response_data = json.loads(response.text)

    if response_data["logo"] is None:
        logo = "https://bit.ly/3xjcvgK"
    else:
        logo = response_data["logo"]

    application = Application(
        name=name,
        title=title,
        location=location,
        notes=notes,
        status=status,
        logo=logo,
        date_applied=date,
    )
    application.save()

    messages.success(request, "Created successfully")

    return redirect("application")


@login_required(login_url="login")
def update_application(request, id):
    """Get apllication id  and update application object"""
    application = Application.objects.get(id=id)
    if request.method != "POST":
        return redirect("application")
    application.name = request.POST.get("name")
    application.title = request.POST.get("title")
    application.location = request.POST.get("location")
    application.notes = request.POST.get("notes")
    application.status = request.POST.get("status")
    application.date_applied = request.POST.get("date")
    application.save()

    messages.success(request, "Updated successfully")

    return redirect("application")


@login_required(login_url="login")
def delete_application(request, id):
    """Get apllication id and delete application"""
    application = Application.objects.get(id=id)
    application.delete()
    messages.success(request, "Deleted successfully")
    return redirect("application")
