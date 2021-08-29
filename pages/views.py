from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView,)
from django.urls import reverse_lazy
# from accounts.models import User

class HomePageView(TemplateView):
    template_name = 'index.html'
