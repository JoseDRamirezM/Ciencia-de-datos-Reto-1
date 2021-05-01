from django.urls import path

from . import views

app_name = "dataset_visual"

urlpatterns = [
    path("", views.index, name="index"),
    path("query", views.render_query, name="query"),
    path("query_params", views.query_params, name="query_params"),

]
