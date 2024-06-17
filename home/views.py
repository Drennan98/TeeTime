from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import GolfCourse
from .forms import GolfCourseForm

# Create your views here.

# Class based views 
class GolfCourseListView(ListView):
    model = GolfCourse
    template_name = "home/golfcourse_list.html"

class GolfCourseDetailView(DetailView):
    model = GolfCourse 
    template_name = "home/golfcourse_detail.html"

class GolfCourseCreateView(CreateView):
    model = GolfCourse
    form_class = GolfCourseForm
    template_name = "home/golfcourse_form.html"
    success_url = reverse_lazy("golfcourse_list")

class GolfCourseUpdateView(UpdateView):
    model = GolfCourse 
    form_class = GolfCourseForm
    template_name = "home/golfcourse_form.html"
    success_url = reverse_lazy("golfcourse_list")

class GolfCourseDeleteView(DeleteView):
    model = GolfCourse 
    template_name = "home/golfcourse_confirm_delete.html"
