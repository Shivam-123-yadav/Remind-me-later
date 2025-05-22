import re
from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    return render(request, "hello/log_message.html", {"form": form})

class LogMessageDeleteView(DeleteView):
    model = LogMessage
    success_url = reverse_lazy("home")
    template_name = "hello/logmessage_confirm_delete.html"
