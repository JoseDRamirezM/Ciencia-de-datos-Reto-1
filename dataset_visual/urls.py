from django.urls import path

from . import views

app_name = "dataset_visual"

urlpatterns = [
    path("", views.index, name="index"),
    path("query", views.render_query, name="query"),
    path("query_params_1", views.query_params_1, name="query_params_1"),
    path("query_params_2", views.query_params_2, name="query_params_2"),
    path("query_params_3", views.query_params_3, name="query_params_3"),
]
