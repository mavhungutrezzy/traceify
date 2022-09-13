from django.urls import path

from . import views

urlpatterns = [
    path("application/", views.application, name="application"),
    path("application/create", views.create_application, name="create_application"),
    path(
        "application/update/<int:id>",
        views.update_application,
        name="update_application",
    ),
    path(
        "application/delete/<int:id>",
        views.delete_application,
        name="delete_application",
    ),
]
