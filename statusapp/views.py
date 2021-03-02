from django.shortcuts import render

from django.views.generic import CreateView
from .forms import StatusMessageModelForm

# Create your views here.

class StatusMessageCreateView(CreateView):
    form_class = StatusMessageModelForm
    template_name = 