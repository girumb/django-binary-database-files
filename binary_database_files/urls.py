from django.urls import re_path
from binary_database_files import views

app_name = "binary_database_files"
urlpatterns = [
    re_path(r"^files/(?P<name>.+)$", views.serve_mixed, name="database_file"),
]
