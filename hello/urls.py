from django.urls import path
from hello import views
from .views import LogMessageDeleteView

urlpatterns = [
    path("", views.HomeListView.as_view(
        queryset=views.LogMessage.objects.order_by("-log_date")[:5],
        context_object_name="message_list",
        template_name="hello/home.html",
    ), name="home"),
    path("about/", views.about, name="about"),
    path("log/", views.log_message, name="log"),
    path("message/<int:pk>/delete/", LogMessageDeleteView.as_view(), name="delete_message"),
]

